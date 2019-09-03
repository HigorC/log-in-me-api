import jwt
import datetime
from flask import jsonify

def createToken():
    token = jwt.encode({
        'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=300)
    }, "loginme", algorithm='HS256')

    return token.decode("utf-8")

def authenticateToken(token):
    try:
        jwt.decode(token, "loginme", algorithms='HS256')
        print(">> Autenticado!")
        return True
    except jwt.exceptions.InvalidSignatureError:
        print("[X] >> Assinatura inválida...")
        return False
    except jwt.exceptions.ExpiredSignatureError:
        print("[X] >> O Token expirou.")
        return False