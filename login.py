import db.mongo_connection as mongo_connection
from flask import abort, request
import db.querys as querys
from bson.json_util import dumps
import datetime
import utils.md5_manager as md5_manager

def login(user):
    typeOfLogin = getTypeOfLogin(user)

    passwordEncrypted = md5_manager.encrypt(request.json.get("password"))

    if typeOfLogin == "email":
        return genericLogin("email",user.get("email"), passwordEncrypted)
    else:
        return genericLogin("username",user.get("username"), passwordEncrypted)

def getTypeOfLogin(user):
    if user.get("password") != None:
        if user.get("email") != None:
            return "email"
        elif user.get("username") != None:
            return "username"
        else:
            abort(400, 'É necessário enviar um objeto contendo as seguintes informações: {email ou username, password}.')
    else:
        abort(400, 'É necessário enviar um objeto contendo as seguintes informações: {email ou username, password}.')

def genericLogin(typeLogin, login, password):
    qtdFound = querys.getQtdByQuery({
        typeLogin: login
    })

    if qtdFound == 0:
        abort(400, 'Não existe um usuário com este ' + typeLogin)

    userFounded = querys.findAndUpdate({
        typeLogin: login,
        "password": password
    },{
        "last_access": datetime.datetime.now()
    })

    if userFounded == None:
        abort(400, 'A senha informada está incorreta.')

    return dumps(userFounded)