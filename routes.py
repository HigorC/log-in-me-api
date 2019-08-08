import app_flask as app_flask

import os
from flask import Blueprint, Flask, request, jsonify

import db.mongo_connection as mongo_connection

app_blueprint = Blueprint('routes',__name__)

@app_blueprint.route("/itWorks")
def defaultRoute():
    return "Yes, it works!"

@app_blueprint.route("/create", methods=['POST'])
def createNewUser():
    if (request.json.get("email") == None or
        request.json.get("user") == None or
        request.json.get("password") == None):
        raise Exception("É necessário enviar um objeto contendo as seguintes informações: {email, user, password}!")

    client = mongo_connection.getClient()
     
    userCreated = client["fakeapi"]["users"].insert_one({
        "email": request.json.get("email"),
        "user": request.json.get("user"),
        "password": request.json.get("password")
    }) 

    return jsonify({"userCreatedId": str(userCreated.inserted_id)})