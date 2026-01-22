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

app.get("/movies/{id}", tags=["root"])
def read_movies(id:int):
    for movie in movies:
        if movie["id"] = id
           return movie
    return movie

app.get("/ejemplo", tags=["root"])
def read_ejemplo():
    return HTMLResponse("<h1>Mi página con HTML</h1>")

# parametros dentro de llaves
app.get("/lista/{id}", tags=["root"])
def read_lista(id: int):
    return id


~~~

## 07. Parámetros Query | Curso de Introducción a FastAPI 2024

https://www.youtube.com/watch?v=C61djwbPCew&list=PLHftsZss8mw7pSRpCyd-TM4Mu43XdyB3R&index=8



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


# pasar parametros y devolver un elemento del array movies
app.get("/movies/{id}", tags=["root"])
def read_movies(id:int):
    for movie in movies:
        if movie["id"] = id
           return movie
    return movie

app.get("/ejemplo", tags=["root"])
def read_ejemplo():
    return HTMLResponse("<h1>Mi página con HTML</h1>")

# parametros dentro de llaves
app.get("/lista/{id}", tags=["root"])
def read_lista(id: int):
    return id


# parametros query se pasa por el parametro de la funcion
app.get("/lista/", tags=["root"])
def get_movie_by_category(cagegory: str,year: int):
    for movie in movies:
        if movie["category"] = category
           return movie
    return movie

~~~

## 08. Método POST | Curso de Introducción a FastAPI 2024

https://www.youtube.com/watch?v=KDIy2bxDNlQ&list=PLHftsZss8mw7pSRpCyd-TM4Mu43XdyB3R&index=9


~~~
from fastapi import FastAPI,Body
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


# pasar parametros y devolver un elemento del array movies
app.get("/movies/{id}", tags=["root"])
def read_movies(id:int):
    for movie in movies:
        if movie["id"] = id
           return movie
    return movie

app.get("/ejemplo", tags=["root"])
def read_ejemplo():
    return HTMLResponse("<h1>Mi página con HTML</h1>")

# parametros dentro de llaves
app.get("/lista/{id}", tags=["root"])
def read_lista(id: int):
    return id


# parametros query se pasa por el parametro de la funcion
app.get("/lista/", tags=["root"])
def get_movie_by_category(cagegory: str,year: int):
    for movie in movies:
        if movie["category"] = category
           return movie
    return movie

# metodo post
@app.post("/movies",tags=['Movies'])
def create_movie(id:int =Body(),
                 title: str=Body(),
                 overview:srt=Body(),
                 year:int=Body(),
                 rating:float=Body(),
                 category:str=Body()):
     movies.append({
        'id':id,
        'title':title,
        'overview':overview,
        'year': year,
        'rating': rating,
        'category': category
     })
     return movies 



~~~

## 09. Método PUT y DELETE | Curso de Introducción a FastAPI 2024

https://www.youtube.com/watch?v=MFD0Gne0S54&list=PLHftsZss8mw7pSRpCyd-TM4Mu43XdyB3R&index=10


~~~
from fastapi import FastAPI,Body
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


# pasar parametros y devolver un elemento del array movies
app.get("/movies/{id}", tags=["root"])
def read_movies(id:int):
    for movie in movies:
        if movie["id"] = id
           return movie
    return movie

app.get("/ejemplo", tags=["root"])
def read_ejemplo():
    return HTMLResponse("<h1>Mi página con HTML</h1>")

# parametros dentro de llaves
app.get("/lista/{id}", tags=["root"])
def read_lista(id: int):
    return id


# parametros query se pasa por el parametro de la funcion
app.get("/lista/", tags=["root"])
def get_movie_by_category(cagegory: str,year: int):
    for movie in movies:
        if movie["category"] == category
           return movie
    return movie

# metodo post
@app.post("/movies",tags=['Movies'])
def create_movie(id:int =Body(),
                 title: str=Body(),
                 overview:srt=Body(),
                 year:int=Body(),
                 rating:float=Body(),
                 category:str=Body()):
     movies.append({
        'id':id,
        'title':title,
        'overview':overview,
        'year': year,
        'rating': rating,
        'category': category
     })
     return movies 

# metodo put
@app.put("/movies/{id}",tags=['Movies'])
def update_movie(id:int,
                 title: str=Body(),
                 overview:srt=Body(),
                 year:int=Body(),
                 rating:float=Body(),
                 category:str=Body()):
    for movie in movies:
        if movie["id"] == id
           movie['title'] = title
           movie['overview'] = overview
           movie['year'] = year
           movie['rating'] = rating
           movie['category'] = category
    return movies

# metodo delete
@app.delete("/movies/{id}",tags=['Movies'])
def delete_movie(id:int):
     for movie in movies:
        if movie["id"] == id
            movies.remove(movie)

    return movies

~~~

## 10. Modelos de datos | Curso de Introducción a FastAPI 2024

https://www.youtube.com/watch?v=2DL8wqRjfKM&list=PLHftsZss8mw7pSRpCyd-TM4Mu43XdyB3R&index=11



pydantic liberia para validar los datos


~~~
from fastapi import FastAPI,Body
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from typing import Optional, List

app = FastAPI()

class Movie(BaseModel):
     id: Optional[int] = None,
     title: str,
     overview: str,
     rating: float,
     category: str

class MovieUpdate(BaseModel):
     title: str,
     overview: str,
     rating: float,
     category: str

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


# pasar parametros y devolver un elemento del array movies
app.get("/movies/{id}", tags=["root"])
def read_movies(id:int):
    for movie in movies:
        if movie["id"] = id
           return movie
    return movie

app.get("/ejemplo", tags=["root"])
def read_ejemplo():
    return HTMLResponse("<h1>Mi página con HTML</h1>")

# parametros dentro de llaves
# list[movie] en minusculas es totaltemente valido
# luego esta List[Movie] desde typing desde pydantic
app.get("/lista/{id}", tags=["root"])
def read_lista(id: int) ->list[Movie]:
    return id


# parametros query se pasa por el parametro de la funcion
app.get("/lista/", tags=["root"])
def get_movie_by_category(cagegory: str,year: int):
    for movie in movies:
        if movie["category"] == category
           return movie
    return movie

# metodo post, utilizamos pydantic
@app.post("/movies",tags=['Movies'])
def create_movie(movie: Movie) ->List[Movie]:
     movies.append(movie.model_dump())
     return movies 

# metodo put
@app.put("/movies/{id}",tags=['Movies'])
def update_movie(id:int, movie:Movie):
    for movie in movies:
        if movie["id"] == id
           movie['title'] = movie.title
           movie['overview'] = movie.overview
           movie['year'] = movie.year
           movie['rating'] = movie.rating
           movie['category'] = movie.category
    return movies

# metodo delete
@app.delete("/movies/{id}",tags=['Movies'])
def delete_movie(id:int):
     for movie in movies:
        if movie["id"] == id
            movies.remove(movie)

    return movies


~~~











