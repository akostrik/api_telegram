#!/usr/bin/python

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

from dotenv import load_dotenv
load_dotenv()  # take environment variables from .env.

uri = "mongodb+srv://anna:1AQ2ZS3ED@cluster0.fnbrrzu.mongodb.net/?retryWrites=true&w=majority"
# импортирует объект MongoClient из PyMongo, создает экземпляр клиента :
clientDB = MongoClient(uri, server_api=ServerApi('1')) 
try:
    clientDB.admin.command('ping')
    print("You successfully connected to MongoDB")
except Exception as e:
    print(e)

print(os.environ)
#os.getenv


# messagesDB = clientDB["messsagesBD"]
# collections = messagesDB.list_collection_names()
# print('\ncollections : ')
# print(collections)

# collection1 = messagesDB.collection1
# print('\ncollection : ')
# print(collection1)

#message = {
#"text": "text message 1",	
#"date": "2023-04-14",
#}
#id = collection1.insert_one(message).inserted_id
#print('\nid inserted message : ')
#print(id)

# print('\ncollection.find_one : ')
# print(collection.find_one({"Created": "collection1"}))


# import asyncio
# from telethon import TelegramClient

# api_id = 356016
# api_hash = 'a8eb9553bc3789a544de55cc91912716'
# clientTG = TelegramClient('anon', api_id, api_hash)
# #channel = 'stalin_gulag'
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

