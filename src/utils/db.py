from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

Mongo_URL = os.getenv("DB_CONNECTION")
DB_NAME = os.getenv("DB_NAME")

client = MongoClient(Mongo_URL)

database = client[DB_NAME]
collection = database.transactions