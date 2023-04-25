#!/usr/bin/python

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv()) # take env variables from .env
MONGO_URI1 = os.environ.get("MONGO_URI1")
MONGO_ID   = os.environ.get("MONGO_ID")
MONGO_PWD  = os.environ.get("MONGO_PWD")
MONGO_URI2 = os.environ.get("MONGO_URI2")
MONGO_URI  = MONGO_URI1 + MONGO_ID + ':' + MONGO_PWD + MONGO_URI2

# импортирует объект MongoClient из PyMongo, создает экземпляр клиента :
clientDB = MongoClient(MONGO_URI, server_api=ServerApi('1')) 
try:
    clientDB.admin.command('ping')
    print("You successfully connected to MongoDB")
except Exception as e:
    print(e)

messagesDB = clientDB["messsagesBD"]
collections = messagesDB.list_collection_names()
collection_msg = messagesDB.messages

msg = {
"text": "message from ann",	
"date": "2023-04-25",
}
id = collection_msg.insert_one(msg).inserted_id
print('\nid inserted message : ' + str(id))


# import asyncio
# from telethon import TelegramClient

# api_id = 356016
# api_hash = 'a8eb9553bc3789a544de55cc91912716'
# clientTG = TelegramClient('anon', api_id, api_hash)
# #channel = 'good_channel'
# group = 'blues34'

# async def func():
# 	me = await clientTG.get_me()
# 	print('I am telegram user: ' + me.username + ' ' + me.phone)
# 	await clientTG.send_message(group, 'Hello from python')
# 	async for message in clientTG.iter_messages(group):
# 		print(message.id, message.text)
# 		messagesDB.users.insert(message)
# with clientTG:
# 	clientTG.loop.run_until_complete(func())

