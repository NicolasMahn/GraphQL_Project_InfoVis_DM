from pymongo import MongoClient
from config import MONGO_URI, MONGO_DB_NAME

client = MongoClient(MONGO_URI)
db = client[MONGO_DB_NAME]

def get_collection(collection_name):
    return db[collection_name]

def insert_one(collection_name, document):
    return get_collection(collection_name).insert_one(document).inserted_id

def find_one(collection_name, query):
    return get_collection(collection_name).find_one(query)

def find_all(collection_name):
    return list(get_collection(collection_name).find())
