from flask import abort
import utils.exception_messages as exception_messages
import db.querys as querys
import re
import requests
import os

def validateRequest(request):
	if(request == None  or request.get("user") == None or request.get("application") == None):
		abort(400, exception_messages.getMsgRequisicaoInvalida())

def validateUser(user, application):
	validateRequiredParametersToCreate(user)
	validateIfUserAlreadyExists(user, application)        

def validateRequiredParametersToCreate(user):
	email = user.get("email")
	username = str(user.get("username"))
	password =  str(user.get("password"))

	if (email == None or not email.strip() or isEmailInvalidByRegex(email) or
		username == None or not username.strip() or len(username) < 4 or
		password == None or not password.strip() or len(password) < 4):
		print("[X] >>  O Objeto passado na requisição é inválido!")
		abort(400, exception_messages.getMsgRequisicaoInvalida())
		
def validateRequiredParametersToLogin(user):
	email = user.get("email")
	username = str(user.get("username"))
	password =  str(user.get("password"))

	if ((email == None or not email.strip() or isEmailInvalidByRegex(email)) and
		(username == None or not username.strip() or len(username) < 4) or
		password == None or not password.strip() or len(password) < 4):
		print("[X] >> O Objeto passado na requisição é inválido!")
		abort(400, exception_messages.getMsgRequisicaoInvalida())

def validateIfUserAlreadyExists(user, application):
	if (querys.getQtdByQuery({"email": user.get("email")}, application) > 0):
		print("[X] >> Já existe um usuário com este email!")
		abort(400, 'Já existe um usuário com este email!')

	if (querys.getQtdByQuery({"username": user.get("username")}, application) > 0):
		print("[X] >> Já existe um usuário com este nome de usuário!")
		abort(400, 'Já existe um usuário com este nome de usuário!')

def isEmailInvalidByRegex(email):
    return re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email) == None

def isTokenValid(token):
	print(">> Validando Token JWT...")

	if (token == None):
		print(">> Sem Token na requisição!")
		return False, 403, exception_messages.getMsgTokenInexistente()
    
	headers = {"authorization": token}

	url_to_authenticate_token = os.environ.get("URL_TO_AUTHENTICATE_TOKEN", "http://localhost:5000/authenticateToken")

	response = requests.get(url_to_authenticate_token, headers=headers)

	if (response.status_code != 200):
		if response.json().get("sub_status") == 1 or response.json().get("sub_status") == 3:
			print("[x] >> Token inválido!")
			return False, 403, response.json()["msg"]
		elif response.json().get("sub_status") == 2:
			print("[x] >> Token expirado!")
			return False, 403, "token_expired"
	else:
		print(">> Token validado!")
		return True, 200, "Valided"