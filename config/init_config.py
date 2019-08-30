import requests
import json

def createAccountOnLocksmith():
    print(">> Criando conta no Locksmith...")

    headers = {
        'Content-type': 'application/json',
        'Accept': 'text/plain'
    }

    try:
        r = requests.post("http://localhost:5000/createUser",
                        data = json.dumps({
                            "email":"login@me.com",
                            "username":"loginme",
                            "password":"1234"}),
                        headers = headers)
    except:
        print("erro, proval conta ja existe")

def loginOnLocksmith():
    print(">> Logando no Locksmith...")

    headers = {
        'Content-type': 'application/json',
        'Accept': 'text/plain'
    }

    r = requests.post("http://localhost:5000/login",
                    data = json.dumps({
                        "email":"login@me.com",
                        "username":"loginme",
                        "password":"1234"}),
                    headers = headers)

    print(r.json)

# createAccountOnLocksmith()