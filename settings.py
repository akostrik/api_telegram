#!/usr/bin/python

import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv()) # take environment variables from .env

MONGO_PWD  = os.environ.get("MONGO_PWD")
MONGO_URI1 = os.environ.get("MONGO_URI1")
MONGO_URI2 = os.environ.get("MONGO_URI2")
MONGO_URI = MONGO_URI1 + MONGO_PWD + MONGO_URI2
print("MONGO_URI = " + MONGO_URI)
