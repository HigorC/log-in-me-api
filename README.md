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

### Fluxo de funcionamento da *API*

O fluxograma abaixo representa o funcionamento do *Log in me* em uma situação perfeita.

![Fluxo Geral](https://github.com/HigorC/log-in-me-api/blob/master/assets/fluxogramas/fluxo_geral.png)

**1, 2.** Se uma *API* qualquer desejar se comunicar com o *Log in me*, o primeiro passo a se tomar é fazer uma requisição para o [Locksmith](https://github.com/HigorC/locksmith), lhe pedindo para gerar um *Token JWT*.

**3.** Com o Token em mãos, a *API* Qualquer o irá setar em seu Header Authorization e fazer uma requisição para o *Log in me*.

**4, 5.** Antes de realizar qualquer processamento, o *Log in me* realiza uma chamada ao [Locksmith](https://github.com/HigorC/locksmith) a fim de validar a autenticidade do *Token* recebido.

**6, 7.** Uma vez tendo sido validado o *Token*, o *Log in me* se comunica com o Banco de Dados *MongoDB*, verificando, validando e salvando o que for necessário.

**8.** Por fim a requisição principal (passo 3) é respondida, retornando um objeto diferente conforme o que foi pedido.
