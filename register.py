import db.mongo_connection as mongo_connection
from flask import abort, request
import db.querys as querys

def createUser(user):
    validateUser(user)

    client = mongo_connection.getClient()
     
    userCreated = client["fakeapi"]["users"].insert_one({
        "email": request.json.get("email"),
        "username": request.json.get("username"),
        "password": request.json.get("password")
    }) 

    return str(userCreated.inserted_id)

def validateUser(user):
   validateRequiredParameters(user)
   validateIfUserAlreadyExists(user)

def validateRequiredParameters(user):
    if (user.get("email") == None or
        user.get("username") == None or
        user.get("password") == None):
        abort(400, 'É necessário enviar um objeto contendo as seguintes informações: {email, username, password}!')

def validateIfUserAlreadyExists(user):
    if (querys.getQtdByQuery({"email": user.get("email")}) > 0):
        abort(400, 'Já existe um usuário com este email!')

    if (querys.getQtdByQuery({"username": user.get("username")}) > 0):
        abort(400, 'Já existe um usuário com este nome de usuário!')