import pymongo

def getClient():
    return pymongo.MongoClient("mongodb+srv://alia:babua@log-in-me-cluster-c8w5d.mongodb.net/test?retryWrites=true&w=majority")