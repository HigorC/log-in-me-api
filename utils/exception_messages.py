def getMsgRequisicaoInvalida():
    return """ Para criar um usuário, o objeto passado na requisição deve seguir a seguinte estrutura:
     {
         "user":{
            "email": exemplo@exemplo.com,
            "username": exemplo,
            "password": 1234.
         },
         "application": "exemplo"
    }

    > O atributo email deve ser um email válido.
    > Os atributos username e password devem possuir ao menos 4 caracteres.
    """

def getMsgTokenInexistente():
   return "Esta API é protegida pelo Locksmith. É necessário setar um Token JWT no Header Authorization da sua requisição."