#!/usr/bin/python
import asyncio
from telethon import TelegramClient

api_id = 356016
api_hash = 'a8eb9553bc3789a544de55cc91912716'
clientTG = TelegramClient('anon', api_id, api_hash)
#channel = 'stalin_gulag'
group = 'blues34'

async def func():
	me = await clientTG.get_me()
	print('I am : ' + me.username + ' ' + me.phone)
	await clientTG.send_message(group, 'Hello from python')
	async for message in clientTG.iter_messages(group):
		print(message.id, message.text)
with clientTG:
	clientTG.loop.run_until_complete(func())

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
uri = "mongodb+srv://anna:1AQ2ZS3ED@cluster0.fnbrrzu.mongodb.net/?retryWrites=true&w=majority"
clientDB = MongoClient(uri, server_api=ServerApi('1'))
try:
    clientDB.admin.command('ping')
    print("You successfully connected to MongoDB")
except Exception as e:
    print(e)

