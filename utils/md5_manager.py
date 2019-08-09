import hashlib 

def encrypt(toEncrypt):
    stringToEncrypt = str(toEncrypt)
    return hashlib.md5(stringToEncrypt.encode()).hexdigest()   