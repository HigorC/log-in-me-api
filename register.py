import db.mongo_connection as mongo_connection
from flask import  request
import datetime
import utils.md5_manager as md5_manager
import utils.validator as validator

def createUser(jsonRequest):
	validator.validateRequest(jsonRequest)

	user = jsonRequest["user"]
	application = jsonRequest["application"]

	validator.validateUser(user)
     
	passwordEncrypted = md5_manager.encrypt(user["password"])

	client = mongo_connection.getClient()

	userCreated = client[application]["users"].insert_one({
        "email": user["email"],
        "username": user["username"],
        "password": passwordEncrypted,
        "created_in": datetime.datetime.now(),
        "last_access": "never"
    }) 
                
	return str(userCreated.inserted_id)