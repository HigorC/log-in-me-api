import pymongo

def getClient():
    # Para uso do MongoDBAtlas
    # return pymongo.MongoClient("mongodb+srv://alia:babua@log-in-me-cluster-c8w5d.mongodb.net/test?retryWrites=true&w=majority")
    # Para uso local
    return pymongo.MongoClient("mongodb://127.0.0.1:27017/?gssapiServiceName=mongodb")