import app_flask as app_flask
from flask import abort, Blueprint, Flask, request, jsonify
import db.mongo_connection as mongo_connection
import register as register
import login as login
import utils.exception_messages as exception_messages
import utils.validator as validator
import json 

app_blueprint = Blueprint('routes',__name__)

@app_blueprint.route("/itWorks")
def defaultRoute():
    return "Yes, it works!"

@app_blueprint.route("/itWorksWithToken", methods=['GET'])
def defaultRouteWithToken():
    return "Yes, it works with Token JWT!"

@app_blueprint.before_request
def verifyToken():
	if request.path != "/itWorks" and request.path != "/isLogged":
		token = request.headers.get("authorization")
		is_valid, status_code, msg = validator.isTokenValid(token)

		if is_valid is False:
			abort(status_code, msg)

@app_blueprint.route("/createUser", methods=['POST'])
def createNewUser():
	idCreated = register.createUser(request.json)
	return jsonify({"userCreatedId": idCreated})

@app_blueprint.route("/login", methods=['POST'])
def loginUser():
	return login.login(request.json)

@app_blueprint.route("/isLogged", methods=['GET'])
def isLogged():
	token = request.headers.get("authorization")
	is_valid, status_code, msg = validator.isTokenValid(token)

	if is_valid is False:
		if msg == "token_expired":
			return jsonify({"isLogged": False})

		abort(status_code, msg)

	return jsonify({"isLogged": True})

@app_blueprint.errorhandler(404)
def errorHandler(error):
    return error