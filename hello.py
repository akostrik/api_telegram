#!/usr/bin/python
import os
import asyncio
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv()) # take env variables from .env


# TELEGRAM ACCES:
from telethon import TelegramClient
ID_TG   = os.environ.get("ID_TG")
HASH_TG = os.environ.get("HASH_TG")
clientTG = TelegramClient('anon', ID_TG, HASH_TG)
channel = 'good_channel'


# MONGO DB ACCES:
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

URI1_BD = os.environ.get("URI1_BD")
ID_BD   = os.environ.get("ID_BD")
PWD_BD  = os.environ.get("PWD_BD")
URI2_BD = os.environ.get("URI2_BD")
uriBD   = URI1_BD + ID_BD + ':' + PWD_BD + URI2_BD

# импортирует объект MongoClient из PyMongo, создает экземпляр клиента :
clientDB = MongoClient(uriBD, server_api=ServerApi('1')) 
try:
	clientDB.admin.command('ping')
	print("You successfully connected to MongoDB")
except Exception as e:
	print(e)

messagesDB      = clientDB["messsagesBD"]
collections     = messagesDB.list_collection_names()
collection_msgs = messagesDB.messages


# READ TG MESSAGES, PUT THEM IM MONGO DB:
async def func_read_insert():
	tg_account = await clientTG.get_me()
	print('You successfully connected to Telegram as user ' + str(tg_account.phone))
	#await clientTG.send_message(channel, 'Hello from python')
	async for msgTG in clientTG.iter_messages(channel):
		msgBD = {
		"text": msgTG.text,
		"date": "2023-04-25",
		}
		if msgTG.text != None:
			collection_msgs.insert_one(msgBD)
with clientTG:
	clientTG.loop.run_until_complete(func_read_insert())





