#!/usr/bin/python
import os
import asyncio
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv()) # take env variables from .env


# TELEGRAM ACCESS:
from telethon import TelegramClient
ID_TG   = os.environ.get("ID_TG")
HASH_TG = os.environ.get("HASH_TG")
clientTG = TelegramClient('anon', ID_TG, HASH_TG)
channel = 'good_channel'


# MONGO DB ACCESS:
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

URI1_MONGO = os.environ.get("URI1_MONGO")
ID_MONGO   = os.environ.get("ID_MONGO")
PWD_MONGO  = os.environ.get("PWD_MONGO")
URI2_MONGO = os.environ.get("URI2_MONGO")
uriMONGO   = URI1_MONGO + ID_MONGO + ':' + PWD_MONGO + URI2_MONGO

# импортирует объект MongoClient из PyMongo, создает экземпляр клиента :
clientDB = MongoClient(uriMONGO, server_api=ServerApi('1')) 
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
ID_OPENAI   = os.environ.get("ID_OPENAI")
openai.api_key = "ID_OPENAI"

# READ TG MESSAGES, PUT THEM IN MONGO DB:
async def func_read_insert():
	tg_account = await clientTG.get_me()
	print('You successfully connected to Telegram as user ' + str(tg_account.phone))
	#await clientTG.send_message(channel, 'Hello from python')
	async for msgTG in clientTG.iter_messages(channel):
		msgBD = {
		"text": msgTG.text,
		"date": msgTG.date,
		}
		if msgTG.text != None:
			collection_msgs.insert_one(msgBD)
with clientTG:
	clientTG.loop.run_until_complete(func_read_insert())





