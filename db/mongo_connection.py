import pymongo
import os

def getClient():
    # Para uso do MongoDBAtlas
    client_url = os.environ.get("MONGO_CLIENT_URL", "mongodb://127.0.0.1:27017/?gssapiServiceName=mongodb")

    return pymongo.MongoClient(client_url)
    # Para uso local
    # return pymongo.MongoClient("mongodb://127.0.0.1:27017/?gssapiServiceName=mongodb")