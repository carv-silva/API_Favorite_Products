# API_Favorite_Products
Esta documentação descreve a estrutura da API de produtos para desafios técnicos.

## Tecnologias utilizadas

* 1 - **Python**
* 2 - **Django**
* 3 - **Django Rest Framework**
* 4 - **Postgresql**
* 5 -  **JWT**
* 6 - **Docker**


### Deploy

1 - Primeira opçao para deploy, faça o download em  https://github.com/carv-silva/API_Favorite_Products
Descompacte e entre na pasta do projeto

1.1 - Segunda opção:

        $  git clone https://github.com/carv-silva/API_Favorite_Products.git

> Essa opção requer o git instalado em sua maquina https://git-scm.com/


 2 - Apos estar no diretorio do projeto realize os seguintes comandos:

    $ python -m venv .venv
    $ source .venv/bin/activate
    $ docker-compose up -d
    $ docker-compose exec web python manage.py migrate
> para esta configuração é necessário que você tenha docker instalado em sua maquina, caso necessario, consulte https://www.docker.com/

### Endpoints

| HTTP Method | URI                                          | Ação
| ---         | ---                                          | ---
| POST        | http://[localhost]/customers/                | Criar um cliente
| GET         | http://[localhost]/customers/[id]            | Obter detalhes do cliente
| PUT         | http://[localhost]/customers/[id]            | Atualizar o cliente
| DELETE      | http://[localhost]/customers/[id]            | Remover o cliente
| POST        | http://[localhost]/favorites/                | Criar um produto favorito
| GET         | http://[localhost]/customers/[id]/favorites  | Obter produtos favoritos do cliente
| DELETE      | http://[localhost]/favorites/[id]            | Excluir um produto favorito
| POST        | http://[localhost]/token/                    | Obter o token
| GET         | [challenge-api](http://challenge-api.luizalabs.com/api/product/?page=1)   |Obter dados dos produtos

#### Ultilizando a API via Curl e  HTTP

>obs: Antes de prosseguir com os passos é necessario a criação de usuario admin que possa ser feito atraves do comando:

    $ docker-compose exec web python manage.py createsuperuser


 * **Obtendo um token**

    >Token: o tempo padrao de um token é de 1 hora, caso  necessario gerar um novo é so acessar a rota
    > [token](http://localhost/token/) ou  [token-refresh](http://localhost/token/refresh/)
    > Voce tambem pode editar o tempo de duracao em  src/settings.py/ACCESS_TOKEN_LIFETIME

    >obs: Usamos o exemplo abaixo para um usuario "admin" e senha "admin" criado no comando anterior

    $ curl -i -H "Content-Type: application/json" -X POST -d '{ "username": "admin", "password": "admin" }' http://127.0.0.1:8000/token/

    <h5>Output:</h5>

    ```
    HTTP/1.1 200 OK
    Date: Thu, 07 Oct 2021 20:33:04 GMT
    Server: WSGIServer/0.2 CPython/3.9.7
    Content-Type: application/json
    Vary: Accept
    Allow: POST, OPTIONS
    X-Frame-Options: DENY
    Content-Length: 438
    X-Content-Type-Options: nosniff
    Referrer-Policy: same-origin

    {"refresh":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTYzMzcyNTE4NCwianRpIjoiNzZkZmUwNjcyMWQ1NDYzZTgyMzU2YmE1YmU
    0MTA1MmYiLCJ1c2VyX2lkIjoxfQ.qcyXUxS98n13Aqdh5l-W2Eubar4R7f5c7D8QSn0fnx8","access":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjMzNjQyMzg0LCJqdGkiOiI4MGVmYjY1NTljZTQ0MWMyYmYzZDIzMjQzY
    2EzODk0ZiIsInVzZXJfaWQiOjF9.WtGrKeyxCVB0mHz2rt47d001HdWrsfWakG5ZLQA7oeE"}

    ```

    >Vamos usar a chave do access para os proximos passos:


* **Inserindo Cliente(POST)**

    $ curl -i -H "Content-Type: application/json" -H "Authorization: Bearer  eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjMzNjUzOTYxLCJqdGkiOiI4OTI2NmE4OWE4NzA0MTRiYjRiMDQwYTdmYjRmZGRjYyIsInVzZXJfaWQiOjF9.T-ctZPMrJ-qLIt_F6g6_sZT4Q0V254btgXZzONDXGkI" -X POST -d '{ "name": "Post Cliente Teste", "email": "postteste@gmail.com"}' http://127.0.0.1:8000/customers/

    <h5>Output:</h5>

    ```
    HTTP/1.1 201 Created
    Date: Thu, 07 Oct 2021 20:44:35 GMT
    Server: WSGIServer/0.2 CPython/3.9.7
    Content-Type: application/json
    Vary: Accept
    Allow: GET, POST, HEAD, OPTIONS
    X-Frame-Options: DENY
    Content-Length: 66
    X-Content-Type-Options: nosniff
    Referrer-Policy: same-origin
    ```

* **Consultar um Cliente(GET)**


    >obs: Para a proxima requisição vamos consultar o cliente criado a cima e utilizaremos os seguintes dados como base:

    ```
    {
        "id": 2,
        "name": "Post Cliente Teste",
        "email": "postteste@gmail.com"
    }
    ```
    $ curl -i -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjMzNjQyNzU3LCJqdGkiOiI3OTIwNWZiODQwZDA0OWE2YTJkN2I2NzU1Njg2MDFjMiIsInVzZXJfaWQiOjF9.ZgqmN8UZoDXyzK5rTGegF9fiVaxRnI34nnl8mamWrfM" http://127.0.0.1:8000/customers/2/

    <h5>Output:</h5>

    ```
    HTTP/1.1 200 OK
    Date: Thu, 07 Oct 2021 20:59:39 GMT
    Server: WSGIServer/0.2 CPython/3.9.7
    Content-Type: application/json
    Vary: Accept
    Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS
    X-Frame-Options: DENY
    Content-Length: 66
    X-Content-Type-Options: nosniff
    Referrer-Policy: same-origin

    {"id":2,"name":"Post Cliente Teste","email":"postteste@gmail.com"}
    ```

* **Atualizar cliente(PUT)**


    $ curl -i -H "Content-Type: application/json" -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjMzNjQyNzU3LCJqdGkiOiI3OTIwNWZiODQwZDA0OWE2YTJkN2I2NzU1Njg2MDFjMiIsInVzZXJfaWQiOjF9.ZgqmN8UZoDXyzK5rTGegF9fiVaxRnI34nnl8mamWrfM" -X PUT -d '{ "name": "Put Cliente Atualizado", "email": "clientePUT@gmal.com" }' http://127.0.0.1:8000/customers/2/

   <h5>Output:</h5>

    ```
    HTTP/1.1 200 OK
    Date: Thu, 07 Oct 2021 21:05:00 GMT
    Server: WSGIServer/0.2 CPython/3.9.7
    Content-Type: application/json
    Vary: Accept
    Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS
    X-Frame-Options: DENY
    Content-Length: 70
    X-Content-Type-Options: nosniff
    Referrer-Policy: same-origin

    {"id":2,"name":"Put Cliente Atualizado","email":"clientePUT@gmal.com"}

    ```

* **Deletando o cliente**

    $ curl -i -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjMzNjQyNzU3LCJqdGkiOiI3OTIwNWZiODQwZDA0OWE2YTJkN2I2NzU1Njg2MDFjMiIsInVzZXJfaWQiOjF9.ZgqmN8UZoDXyzK5rTGegF9fiVaxRnI34nnl8mamWrfM" -X DELETE  http://127.0.0.1:8000/customers/2/

   <h5>Output:</h5>

    ```
    HTTP/1.1 204 No Content
    Date: Thu, 07 Oct 2021 21:10:30 GMT
    Server: WSGIServer/0.2 CPython/3.9.7
    Vary: Accept
    Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS
    X-Frame-Options: DENY
    Content-Length: 0
    X-Content-Type-Options: nosniff
    Referrer-Policy: same-origin

    ```

* **Criando Produto favorito(POST)**

    >obs: Aqui vamos pegar um id de um produto existe para adicionar na lista, caso queira listar os produtos
    > disponivel consultar : [challenge-api](http://challenge-api.luizalabs.com/api/product/?page=1)

    $ curl -i -H "Content-Type: application/json" -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjMzNjQyNzU3LCJqdGkiOiI3OTIwNWZiODQwZDA0OWE2YTJkN2I2NzU1Njg2MDFjMiIsInVzZXJfaWQiOjF9.ZgqmN8UZoDXyzK5rTGegF9fiVaxRnI34nnl8mamWrfM" -d '{ "product_id": "212d0f07-8f56-0708-971c-41ee78aadf2b", "customer": "1" }' -X POST http://127.0.0.1:8000/favorites/

    <h5>Output:</h5>

    ```
    HTTP/1.1 201 Created
    Date: Thu, 07 Oct 2021 21:24:16 GMT
    Server: WSGIServer/0.2 CPython/3.9.7
    Content-Type: application/json
    Vary: Accept
    Allow: GET, POST, HEAD, OPTIONS
    X-Frame-Options: DENY
    Content-Length: 73
    X-Content-Type-Options: nosniff
    Referrer-Policy: same-origin

    {"id":1,"product_id":"212d0f07-8f56-0708-971c-41ee78aadf2b","customer":1}

    ```

* **Listar produtos favoritos do cliente(GET)**

    $ curl -i -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjMzNjQyNzU3LCJqdGkiOiI3OTIwNWZiODQwZDA0OWE2YTJkN2I2NzU1Njg2MDFjMiIsInVzZXJfaWQiOjF9.ZgqmN8UZoDXyzK5rTGegF9fiVaxRnI34nnl8mamWrfM" http://127.0.0.1:8000/customers/1/favorites/


    <h5>Output:</h5>

    ```
    HTTP/1.1 200 OK
    Date: Thu, 07 Oct 2021 21:34:02 GMT
    Server: WSGIServer/0.2 CPython/3.9.7
    Content-Type: application/json
    Vary: Accept
    Allow: GET, HEAD, OPTIONS
    X-Frame-Options: DENY
    Content-Length: 339
    X-Content-Type-Options: nosniff
    Referrer-Policy: same-origin

    {"meta":{"page_number":1,"page_size":100},"results":[{"id":"1","title":"The Walking Dead - Game of the Year Edition","image":"http://challenge-api.luizalabs.com/images/212d0f07-8f56-0708-971c-41ee78aadf2b.jpg","price":149.9,"link":"http://challenge-api.luizalabs.com/api/product/212d0f07-8f56-0708-971c-41ee78aadf2b/","reviewScore":null}]
    ```

* **Deletar produto favorito**

    $ curl -i -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjMzNjQ2NTgxLCJqdGkiOiIxZDBkYzZiZTcyZTE0YmMzOTJjYmM2NGU1NWE2ZjVhZiIsInVzZXJfaWQiOjF9.3Pt9cveG-HSnc-c-ed19Pikx7USu7R2RgccADp0QQo0" -X DELETE http:/127.0.0.1:8000/favorites/1/

    <h5>Output:</h5>

    ```
    HTTP/1.1 204 No Content
    Date: Thu, 07 Oct 2021 21:46:41 GMT
    Server: WSGIServer/0.2 CPython/3.9.7
    Vary: Accept
    Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS
    X-Frame-Options: DENY
    Content-Length: 0
    X-Content-Type-Options: nosniff
    Referrer-Policy: same-origin
    ```


### Testes
>Para realizar os teste da API favor rodar o seguinte comando dentro da pasta do projeto:
    $ docker-compose exec web python manage.py test

* **APITestCase**

    <h5>Output:</h5>

    ```
    Creating test database for alias 'default'...
    System check identified no issues (0 silenced).
    ................
    ----------------------------------------------------------------------
    Ran 16 tests in 5.849s

    OK
    Destroying test database for alias 'default'...
    ```









