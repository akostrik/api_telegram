#!/usr/bin/python
import asyncio
from telethon import TelegramClient

api_id = 356016
api_hash = 'a8eb9553bc3789a544de55cc91912716'
client = TelegramClient('anon', api_id, api_hash)

async def func():
	me = await client.get_me()
	print(me.username)
	print(me.phone)
	#await client.send_message('Totokop', 'Hello')
	async for message in client.iter_messages('+7(969)717-70-31'):
		print(message.id, message.text)
with client:
	client.loop.run_until_complete(func())
