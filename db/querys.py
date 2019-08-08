import db.mongo_connection as mongo_connection
from pymongo import ReturnDocument

def getQtdByQuery(query):
    return findByQuery(query).count()

def findByQuery(query):
    client = mongo_connection.getClient()

    return client["fakeapi"]["users"].find(query)

def getSomeAtributesByQuery(query, atributes):
    client = mongo_connection.getClient()

    return client["fakeapi"]["users"].find(query, atributes)

def findAndUpdate(query, newAtributes):
    client = mongo_connection.getClient()

    return client["fakeapi"]["users"].find_one_and_update(
        query,
        {'$set': newAtributes},
        projection={"password": False},
        return_document=ReturnDocument.AFTER)