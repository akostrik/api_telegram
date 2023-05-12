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

#article = " Эх, мое роскошное и элитное почти двухмесячное пребывание в «хорошей» камере (кофе и две книжки) бессердечно прервано, и меня снова отправили в конец коридора в «плохую» камеру (кипяток и одна книжка). 15 суток ШИЗО - «неправильно представился». Очевидно, начальство не выдержало «Оскара», решив, что две книги в камере И «Оскар» - это слишком. Логично. Но, конечно, не снимает вопроса о том, почему «Оскара» получают одни люди, а в ШИЗО сижу я 😉"
article = "Qui était le bon roi Dagobert Ier ? Tout le monde connaît le « Bon Roi Dagobert » grâce à la chanson française qui l’a popularisé, mais derrière la légende de « la culotte à l’envers », qui était donc ce roi mérovingien ? CHARLOTTE CHAULIN Publié le 26/06/2021 à 8h57 - Mis à jour le 27/06/2021. Le dernier grand roi mérovingien. Né vers l’an 600, Dagobert se voit confier la couronne d’Austrasie par son père, Clotaire II, en 623. À la mort de ce dernier en 629, il se fait reconnaître roi de Neustrie par les nobles du royaume. Quand son frère Charibert, à qui il avait laissé le gouvernement d’une partie de l’Aquitaine et du Languedoc, meurt en 632, Dagobert devient alors l’unique roi des Francs. Pour s’en assurer, il fait même assassiner le fils de Charibert. Pendant les dix années de son règne, Dagobert est le seul maître d’un royaume mérovingien qui s’étend des Pyrénées au Rhin, de la Bretagne à l’Elbe. Il peut compter sur les conseils de l’ancien orfèvre Eloi (le « bon saint Eloi » de la chanson) qui devient son ministre des finances et centralise la frappe de la monnaie dans son palais de Clichy. Dans une volonté d’unifier le royaume, Dagobert fait de Paris sa capitale. Dagobert assoit son autorité Diplomate qui préfère la paix à la guerre, il se montre fin négociateur. Il entretient de bonnes relations avec Byzance et signe un traité de paix perpétuel avec l’empereur Héraclius en 631. Mais cela ne l’empêche pas de mener quelques expéditions militaires pour lutter contre les menaces extérieures. L’année suivante, il détrône un roi wisigoth de l’autre côté des Pyrénées pour y placer quelqu’un de son choix et s’assurer ainsi de sa fidélité. Dagobert fait reconnaître son autorité, par les Saxons, les Gascons ou encore les Bretons, et empêche la division du royaume des Francs. Mais en donnant l’Austrasie à son fils aîné Sigebert III, à la demande de ses conseillers Pépin et Arnould, puis en promettant à son fils Clovis II la Bourgogne et l’Aquitaine, il met à mal l’œuvre de son règne. Son fils n’ayant que 10 ans, le pouvoir est concentré entre les mains des conseillers Pépin de Landen et Arnould de Metz. Pépin, ancêtre de Charlemagne, exerce la fonction de « maire du palais » et inaugure une lignée (les Pippinides) qui s’empare du pouvoir et gouverne à la place des rois. C’est pour cela qu’après Dagobert, les rois mérovingiens seront surnommés les « rois fainéants » et laisseront la place aux Carolingiens. Après sa mort en 639, Dagobert est enterré selon son souhait dans l’abbaye de Saint-Denis et inaugure ainsi la tradition de la nécropole royale. Dagobert portait-il réellement sa culotte à l’envers ? Le bon roi DagobertAvait sa culotte à l'enversLe grand saint Eloi lui ditO mon roi, votre majestéEst mal culottéeC'est vrai lui dit le roije vais la remettre à l'endroit Quel gaffeur ce Dagobert ! Mais le roi mérovingien portait-il réellement sa culotte à l’envers ? Les historiens ne peuvent pas vérifier l’anecdote qui salit son image de roi pour faire de lui un bouffon. Un écrivain du VIIIème siècle, Wulfran de Strasbourg, raconte que le roi Dagobert était myope et qu’il lui arrivait de se prendre les pieds dans le tapis. Les sources concordent à dire qu’il aimait rire. C’est sûrement ce qu’il aurait fait d’ailleurs s’il avait pu entendre la chansonnette... mais c’est bien plus tard qu’elle fut composée, plus de mille ans après sa mort, au XVIIIème siècle. Derrière Dagobert… Louis XVI ! C’est sous l’Ancien Régime, à l’approche de la Révolution française, que sont écrites les paroles du Bon Roi Dagobert. Pourquoi se moquer alors de cet obscur roi mérovingien ? En réalité, ce n’est pas lui qui est visé mais le roi Louis XVI ! Alcoolique, mauvais catholique, le monarque à qui l’on va couper la tête en 1793 est accusé de tous les maux. Il serait si benêt qu’il mettrait même sa culotte à l’envers. Aujourd’hui, tous les écoliers connaissent la comptine qui prend le pauvre Dagobert pour cible. Mais il était impossible pour les détracteurs de la monarchie de pointer du doigt leur véritable coupable et risquer ainsi de funestes représailles. Pour contourner la censure, quoi de mieux qu’emprunter le nom d’un roi que tout le monde a oublié ?"

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
