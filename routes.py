import os
import app_flask as app_flask
from flask import Blueprint, Flask, request, jsonify
import db.mongo_connection as mongo_connection
import register as register
import login as login
 
app_blueprint = Blueprint('routes',__name__)

@app_blueprint.route("/itWorks")
def defaultRoute():
    return "Yes, it works!"

@app_blueprint.route("/create", methods=['POST'])
def createNewUser():
    idCreated = register.createUser(request.json)
    return jsonify({"userCreatedId": idCreated})

@app_blueprint.route("/login", methods=['POST'])
def loginUser():
    return jsonify({"user": login.login(request.json)})

@app_blueprint.errorhandler(404)
def errorHandler(error):
    return error