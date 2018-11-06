
# API REST Agendamento

## Tecnologias
Neste projeto foi usado as seguintes tecnologias,
Django framework,
Django REST Framework,
Linguagem de programação Python e
Banco de dados Sqlite3.

## Sobre o Projeto
[Django](https://www.djangoproject.com/) é um framework muito estável onde existe uma comunidade sempre trabalhando para melhorias
deixando sempre atualizado, corrigindo bugs e melhorando a segurança.

[Django REST](http://www.django-rest-framework.org/) foi usado para criar o API REST responsável pela integração, esse framework é bem robusto e atende as necessidades de um grande ou pequeno projeto umas da vantagens dele é a grande familiaridade com o Django tornando assim uma programação mais simples para manutenção e melhorias do projeto

Banco de dados [SQLite](https://www.sqlite.org/) foi usado neste projeto por ser default do Django e também  por ser um projeto pequeno ele atende todas as necessidades de forma aceitável.

### Manipuladores e Roteamento
**Método**|**URL**|**Ação**|**filtragem**
:--:|:--:|:--:|:--:
POST|`http://127.0.0.1:8000/salas/`|cria uma nova sala|false
GET|`http://127.0.0.1:8000/salas/`|lista as salas|true
GET|`http://127.0.0.1:8000/salas/<id_sala>/`|Detalhe da sala|false
PUT|`http://127.0.0.1:8000/salas/<id_sala>/`|atualiza uma sala|false
DELETE|`http://127.0.0.1:8000/salas/<id_sala>/`|deleta uma sala|false
POST|`http://127.0.0.1:8000/agendas/`|cria um novo agendamento|false
GET|`http://127.0.0.1:8000/agendas/`|lista os agendamentos|true
GET|`http://127.0.0.1:8000/agendas/<id_agenda>/`|Detalhe do agendamento|false
PUT|`http://127.0.0.1:8000/agendas/<id_agenda>/`|atualiza um agendamento|false
DELETE|`http://127.0.0.1:8000/agendas/<id_agenda>/`|deleta um agendamento|false

**Estrutura Sala**

```json
    {
        "titulo": "Sala 01", // titulo da sala
        "capacidade": 10 // capacidade de pessoas suportada na sala
    }
```

**Estrutura Agenda**

```json
    { 
        "titulo": "Reunião de alinhamento", // titulo da reuniao
        "inicio": "2018-11-04T15:00:00Z", // inicio da reuniao
        "fim": "2018-11-01T18:00:00Z", // fim da reuniao
        "qtd_pessoas": 5, // quantidade de pessoas que irao participar da reunião
        "sala": 1 // id da sala 
    }
```

## Filtragem

Para executar uma filtragem é preciso passar como parâmetro o atributo desejado que deseja filtrar eo valor na requisição, por exemplo:

`http://127.0.0.1:8000/agendas/?data_inicio=2018-01-01T16:00:00Z`

## Como rodar

Criei uma [docker](https://hub.docker.com/) e disponibilizei ela no [hub.docker.com](https://hub.docker.com/r/arturribeiro/solicitasala/)

Então para rodar o projeto é só executar o comando:

docker run -d -p 8000:8000 arturribeiro/solicitasala

Para a execução dos teste unitários é preciso entrar na docker com o seguinte comando:

docker exec -it id_da_docker bash 

E logo em seguida dentro da docker:

python manage.py test -v 2

## Extra
No projeto contém um diretório /[postman](https://www.getpostman.com/), nele contém uma collection com todas requisições montadas para facilitar o processo de teste, é só importar no Postman.