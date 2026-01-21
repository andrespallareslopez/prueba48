# ayuda tutoriales info fastapi

## Presentación del #curso de #FastAPI - #Backend con #Python

PabloEsDev

## 01. ¿Qué es FastAPI? | #Curso de Introducción a #FastAPI 2024 - #Backend con #Python

https://www.youtube.com/watch?v=gIdLS_ShdnM&list=PLHftsZss8mw7pSRpCyd-TM4Mu43XdyB3R&index=2



- path operations
- validacion de datos
- documentacion - open api

Marco utilizado por FAstAPI
- Starlette
- Pydantic
- Uvicorn


~~~
from typing import Union

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


~~~

## 02. Instalación de herramientas de trabajo | Curso de Introducción a FastAPI 2024

https://www.youtube.com/watch?v=dk0BG_PDH7s&list=PLHftsZss8mw7pSRpCyd-TM4Mu43XdyB3R&index=3


~~~

python -m venv .venv

# luego vamos a la carpeta .venv y activamos el entorno virtual con activate

# una vez instalado el entorno virtual instalamos las dependencias:
pip install fastapi uvicorn


~~~

## 03. Creación de primera aplicación | Curso de Introducción a FastAPI 2024

https://www.youtube.com/watch?v=Y253y5t_9mY&list=PLHftsZss8mw7pSRpCyd-TM4Mu43XdyB3R&index=4

PabloEsDev


~~~

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}



~~~

para ejecutar y levantar la aplicacion:


~~~     
# main es el nombre del archivo
# app es el nombre de la instancia de FastAPI
# --reload es para que se reinicie automaticamente al guardar
uvicorn main:app --reload

# alternativas al comando anterior
uvicorn main:app --reload --host [IP_ADDRESS] --port 8000

uvicorn main:app --reload --host [0.0.0.0] --port 8000 --workers 2

~~~

## 04. Documentación automática | Curso de Introducción a FastAPI 2024

https://www.youtube.com/watch?v=5gwCOje67Js&list=PLHftsZss8mw7pSRpCyd-TM4Mu43XdyB3R&index=5

swagger


~~~ 
from fastapi import FastAPI

app = FastAPI()

app.title = "Mi API con FastAPI"
app.version = "1.0.0"   



@app.get("/", tags=["root"])
def read_root():
    return {"Hello": "World"}


~~~ 

http://localhost:8000/docs

http://localhost:8000/redoc

## 05. Uso de método GET | Curso de Introducción a FastAPI 2024

https://www.youtube.com/watch?v=HT4UF-Lse_M&list=PLHftsZss8mw7pSRpCyd-TM4Mu43XdyB3R&index=6



~~~ 
from fastapi import FastAPI
from fastapi.responses import HTMLResponse


app = FastAPI()

# crear una lista de movies

movies = [
    {
        "title": "The Matrix",
        "year": 1999,
        "rating": 8.7,
        "category": "Sci-Fi"
    },
    {
        "title": "The Godfather",
        "year": 1972,
        "rating": 9.2,
        "category": "Crime"
    },
    {
        "title": "The Dark Knight",
        "year": 2008,
        "rating": 9.0,
        "category": "Action"
    }
]


app.title = "Mi API con FastAPI"
app.version = "1.0.0"   


# devolvemos un diccionario
@app.get("/", tags=["root"])
def read_root():
    return {"Hello": "World"}

app.get("/movies", tags=["root"])
def read_movies():
    return {"Hello": "World"}

app.get("/ejemplo", tags=["root"])
def read_ejemplo():
    return HTMLResponse("<h1>Mi página con HTML</h1>")


app.get("/lista", tags=["root"])
def read_lista():
    return movies

~~~


## 06. Parámetros de Ruta | Curso de Introducción a FastAPI 2024

https://www.youtube.com/watch?v=ALbfhifkFas&list=PLHftsZss8mw7pSRpCyd-TM4Mu43XdyB3R&index=7


~~~ 
from fastapi import FastAPI
from fastapi.responses import HTMLResponse


app = FastAPI()

# crear una lista de movies

movies = [
    {
        "title": "The Matrix",
        "year": 1999,
        "rating": 8.7,
        "category": "Sci-Fi"
    },
    {
        "title": "The Godfather",
        "year": 1972,
        "rating": 9.2,
        "category": "Crime"
    },
    {
        "title": "The Dark Knight",
        "year": 2008,
        "rating": 9.0,
        "category": "Action"
    }
]


app.title = "Mi API con FastAPI"
app.version = "1.0.0"   


# devolvemos un diccionario
@app.get("/", tags=["root"])
def read_root():
    return {"Hello": "World"}

app.get("/movies", tags=["root"])
def read_movies():
    return {"Hello": "World"}

app.get("/ejemplo", tags=["root"])
def read_ejemplo():
    return HTMLResponse("<h1>Mi página con HTML</h1>")


app.get("/lista", tags=["root"])
def read_lista():
    return movies

~~~

