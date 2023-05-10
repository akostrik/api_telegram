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
print(ID_TG)
print(HASH_TG) 
clientTG = TelegramClient('anon', ID_TG, HASH_TG)
channel = 'good_channel'

# MONGO DB ACCESS:
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

PRF_MG = str(os.environ.get("PRF_MG"))
ID_MG  = str(os.environ.get("ID_MG"))
PWD_MG = str(os.environ.get("PWD_MG"))
SUF_MG = str(os.environ.get("SUF_MG"))
uriMG   = PRF_MG+ID_MG+":" + urllib.parse.quote(PWD_MG) + SUF_MG
print (uriMG)

clientDB = MongoClient(uriMG, server_api=ServerApi('1')) 
try:
	clientDB.admin.command('ping')
	print("You successfully connected to MongoDB")
except Exception as e:
	print(e)

messagesDB      = clientDB["messsagesBD"]
collections     = messagesDB.list_collection_names()
collection_msgs = messagesDB.messages


# GPT ACCESS:
import openai
KEY_OPENAI   = os.environ.get("KEY_OPENAI")
openai.api_key = KEY_OPENAI
model_engine = "text-davinci-003"


# #text = " Эх, мое роскошное и элитное почти двухмесячное пребывание в «хорошей» камере (кофе и две книжки) бессердечно прервано, и меня снова отправили в конец коридора в «плохую» камеру (кипяток и одна книжка). 15 суток ШИЗО - «неправильно представился». Очевидно, начальство не выдержало «Оскара», решив, что две книги в камере И «Оскар» - это слишком. Логично. Но, конечно, не снимает вопроса о том, почему «Оскара» получают одни люди, а в ШИЗО сижу я 😉"

# READ TG MESSAGES, PUT THEM IN MONGO DB:
async def func_read_insert():
	tg_account = await clientTG.get_me()
	print('You successfully connected to Telegram as user ' + str(tg_account.phone))
	#await clientTG.send_message(channel, 'Hello from python')
	async for msgTG in clientTG.iter_messages(channel):
		if msgTG.text != None:
			text = " “”” " + msgTG.text + " “”” "
			summary = openai.Completion.create(engine=model_engine, prompt="Give me a very short summary, as short as possible, of this text (no more than 15 words please), in English" + text).choices[0].text
#			msgBD = {
#			"text"   : msgTG.text,
#			"date"   : msgTG.date,
#			"summary": summary,
#			}
			collection_msgs.insert_one(msgBD)
with clientTG:
	clientTG.loop.run_until_complete(func_read_insert())
