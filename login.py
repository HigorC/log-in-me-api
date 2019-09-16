import db.mongo_connection as mongo_connection
from flask import abort, request
import db.querys as querys
from bson.json_util import dumps
import datetime
import utils.md5_manager as md5_manager
import utils.exception_messages as exception_messages
import utils.validator as validator
import requests
import json
from bson import json_util
import managers.jwt_manager as jwt_manager

def login(jsonRequest):
    validator.validateRequest(jsonRequest)

    user = jsonRequest["user"]
    application = jsonRequest["application"]

    validator.validateRequiredParametersToLogin(user)

    typeOfLogin = getTypeOfLogin(user)

    passwordEncrypted = md5_manager.encrypt(user["password"])

    if typeOfLogin == "email":
        return genericLogin("email", user["email"], passwordEncrypted, application)
    else:
        return genericLogin("username", user["username"], passwordEncrypted, application)

def getTypeOfLogin(user):
    if user.get("password") != None:
        if user.get("email") != None:
            return "email"
        elif user.get("username") != None:
            return "username"
        else:
            abort(400, exception_messages.getMsgRequisicaoInvalida())
    else:
        abort(400, exception_messages.getMsgRequisicaoInvalida())

def genericLogin(typeLogin, login, password, application):
    qtdFound = querys.getQtdByQuery({
        typeLogin: login
    }, application)

    if qtdFound == 0:
        abort(400, 'Não existe um usuário com este ' + typeLogin)

    userFounded = querys.findAndUpdate({
        typeLogin: login,
        "password": password
    },{
        "last_access": datetime.datetime.now()
    }, application)

    if userFounded == None:
        abort(400, 'A senha informada está incorreta.')

    userFounded["access_token"] = jwt_manager.createToken()

    return json.dumps(userFounded, sort_keys=True, indent=4, default=json_util.default)

def generateLoginTokenInLocksmith():
    headers = {"authorization": request.headers.get("authorization")}
    return requests.get("http://localhost:5000/generateToken/fakeapi", headers=headers)
