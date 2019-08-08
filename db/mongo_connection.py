import pymongo
import os

# A URL de conexão com o MongoDB é pega da seguinte forma:
# > Caso exista uma variável de ambiente chamada [MONGO_CLIENT_URL], esta será usada
# > Se não, a url default do cliente local será utilizada
# Esta variável foi setada no HerokuApp, apontando para o MongoDBAtlas - já com o login e senha setados.
def getClient():
    client_url = os.environ.get("MONGO_CLIENT_URL", "mongodb://127.0.0.1:27017/?gssapiServiceName=mongodb")
    return pymongo.MongoClient(client_url)