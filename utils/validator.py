from flask import abort
import utils.exception_messages as exception_messages
import db.querys as querys
import re
import requests
import os

def validateRequest(request):
    if(request.get("user") == None or request.get("application") == None):
        abort(400, exception_messages.getMsgRequisicaoInvalida())

def validateUser(user):
	validateRequiredParametersToCreate(user)
	validateIfUserAlreadyExists(user)        

def validateRequiredParametersToCreate(user):
	email = user.get("email")
	username = str(user.get("username"))
	password =  str(user.get("password"))

	if (email == None or not email.strip() or isEmailInvalidByRegex(email) or
		username == None or not username.strip() or len(username) < 4 or
		password == None or not password.strip() or len(password) < 4):
		abort(400, exception_messages.getMsgRequisicaoInvalida())
		
def validateRequiredParametersToLogin(user):
	email = user.get("email")
	username = str(user.get("username"))
	password =  str(user.get("password"))

	if ((email == None or not email.strip() or isEmailInvalidByRegex(email)) and
		(username == None or not username.strip() or len(username) < 4) or
		password == None or not password.strip() or len(password) < 4):
		abort(400, exception_messages.getMsgRequisicaoInvalida())

def validateIfUserAlreadyExists(user):
    if (querys.getQtdByQuery({"email": user.get("email")}) > 0):
        abort(400, 'Já existe um usuário com este email!')

    if (querys.getQtdByQuery({"username": user.get("username")}) > 0):
        abort(400, 'Já existe um usuário com este nome de usuário!')

def isEmailInvalidByRegex(email):
    return re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email) == None

def validateTokenBeforeRequest(token):
	if (token == None):
		abort(403, exception_messages.getMsgTokenInexistente())
    
	headers = {"authorization": "Bearer " + token}

	url_to_authenticate_token = os.environ.get("URL_TO_AUTHENTICATE_TOKEN")

	response = requests.get(url_to_authenticate_token, headers=headers)

	if (response.status_code != 200):
		abort(response.status_code, response.json()["msg"])