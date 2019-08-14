# *Log in me (API)*

O ***Log in me*** permite criar e armazenar usuários de diferentes aplicações.

### Instalação

Instalar as libs utilizadas no projeto:

```
pip install flask
pip install pymongo
pip install dnspython
pip install requests
```

### Para rodar
```
python run.js
```
## Funcionamento

Todas as rotas do ***Log in me***, com exceção da rota para verificação de teste (/itWorks) é protegida pelo [Locksmith](https://github.com/HigorC/locksmith). Por isso as requisições devem em seus cabeçalhos o *Header Authorization* com um *Token JWT* gerado pelo [Locksmith](https://github.com/HigorC/locksmith).

As rotas disponíveis são:

* itWorks[GET] - Rota não protegida. Verifica a disponibilidade da aplicação, respondendo uma simples mensagem caso a rota funcione corretamente.
* create[POST] - Rota protegida. Recebe um objeto contendo o usuário a ser criado e a aplicação a qual este faz parte, e o salva no banco de dados. Retorna em caso de sucesso o id do usuário gerado.
* login[POST] - Rota protegida. Recebe um objeto contendo o usuário a ser logado e valida se este existe no banco e se a senha informada está correta.
