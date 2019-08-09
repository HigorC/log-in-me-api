import db.mongo_connection as mongo_connection
from pymongo import ReturnDocument

def getQtdByQuery(query, application):
    return findByQuery(query, application).count()

def findByQuery(query, application):
    client = mongo_connection.getClient()
    return client[application]["users"].find(query)

def getSomeAtributesByQuery(query, atributes, application):
    client = mongo_connection.getClient()
    return client[application]["users"].find(query, atributes)

def findAndUpdate(query, newAtributes, application):
    client = mongo_connection.getClient()
    return client[application]["users"].find_one_and_update(
        query,
        {'$set': newAtributes},
        projection={"password": False},
        return_document=ReturnDocument.AFTER)