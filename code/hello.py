#!/usr/bin/python
import os
import asyncio
import urllib 
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv()) # take env variables from .env


# TELEGRAM ACCESS:
from telethon import TelegramClient
ID_TG   = os.environ.get("ID_TG")
HASH_TG = os.environ.get("HASH_TG")
clientTG = TelegramClient('anon', ID_TG, HASH_TG)
channel = 'good_channel'
#clientTG.send_message(channel, 'Hello from python')

# MONGO DB ACCESS:
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
PRF_MG = str(os.environ.get("PRF_MG"))
ID_MG  = urllib.parse.quote(str(os.environ.get("ID_MG")))
PWD_MG = urllib.parse.quote(str(os.environ.get("PWD_MG")))
SUF_MG = str(os.environ.get("SUF_MG"))
uriMG   = PRF_MG + ID_MG + ":" + PWD_MG + SUF_MG

clientMG = MongoClient(uriMG, server_api=ServerApi('1')) 
try:
	clientMG.admin.command('ping')
	print("Connected to MongoDB")
except Exception as e:
	print(e)
db      	      = clientMG["stage"]
collQueries = db.queries

# OPENAI ACCESS:
import openai
KEY_OPENAI     = os.environ.get("KEY_OPENAI")
openai.api_key = KEY_OPENAI
model_engine   = "text-davinci-003" ###

article = " Эх, мое роскошное и элитное почти двухмесячное пребывание в «хорошей» камере (кофе и две книжки) бессердечно прервано, и меня снова отправили в конец коридора в «плохую» камеру (кипяток и одна книжка). 15 суток ШИЗО - «неправильно представился». Очевидно, начальство не выдержало «Оскара», решив, что две книги в камере И «Оскар» - это слишком. Логично. Но, конечно, не снимает вопроса о том, почему «Оскара» получают одни люди, а в ШИЗО сижу я 😉"
print (article)
for query in collQueries.find():
	prompt = query['text'] + "(in English) " + " “”” " + article + " “”” "
	answer = openai.Completion.create(engine=model_engine, prompt=prompt).choices[0].text
	print (str((str(query['type']) + " : " + str(answer))).replace('\n', ''))

# READ TG MESSAGES, PUT THEM IN MONGO DB:
# clean data ###
#async def func_read_insert():
#	tg_account = await clientTG.get_me()
#	print('Connected to Telegram as user ' + str(tg_account.phone))
#	async for msgTG in clientTG.iter_messages(channel): ###
#		if msgTG.text != None:
#			promptAuthor = collQueries.find_one({'type': 'author'})['text'] + "(in English) " + " “”” " + article + " “”” "
#			# msgTG.text
#			print (promptAuthor)
#			author = openai.Completion.create(engine=model_engine, prompt=promptAuthor).choices[0].text
#			print (author)
#			msgMG = {
#			"text"   : msgTG.text,
#			"date"   : msgTG.date,
#			"domain" : domain,
#			}
			#collectionMsgs.insert_one(msgMG)
#with clientTG:
#	clientTG.loop.run_until_complete(func_read_insert())
