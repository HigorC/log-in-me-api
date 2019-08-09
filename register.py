import db.mongo_connection as mongo_connection
from flask import abort, request
import db.querys as querys
import re
import datetime
import utils.md5_manager as md5_manager

def createUser(user):
    validateUser(user)

    client = mongo_connection.getClient()
     
    passwordEncrypted = md5_manager.encrypt(request.json.get("password"))

    userCreated = client["fakeapi"]["users"].insert_one({
        "email": request.json.get("email"),
        "username": request.json.get("username"),
        "password": passwordEncrypted,
        "created_in": datetime.datetime.now(),
        "last_access": "never"
    }) 

    return str(userCreated.inserted_id)

def validateUser(user):
   validateRequiredParameters(user)
   validateIfUserAlreadyExists(user)

def validateRequiredParameters(user):
    email = user.get("email")
    username = str(user.get("username"))
    password =  str(user.get("password"))

    if (email == None or not email.strip() or isEmailInvalidByRegex(email) or
        username == None or not username.strip() or len(username) < 4 or
        password == None or not password.strip() or len(password) < 4):
        abort(400, 'É necessário enviar um objeto contendo as seguintes informações: {email (validado), username (min 4 caracters), password (min 4 caracters)}.')

def validateIfUserAlreadyExists(user):
    if (querys.getQtdByQuery({"email": user.get("email")}) > 0):
        abort(400, 'Já existe um usuário com este email!')

    if (querys.getQtdByQuery({"username": user.get("username")}) > 0):
        abort(400, 'Já existe um usuário com este nome de usuário!')

def isEmailInvalidByRegex(email):
    return re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email) == None