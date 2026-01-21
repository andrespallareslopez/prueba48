# Proyecto IBIOL

Tenemos una serie de paginas html que son mocks de componentes html hechos con tailwinds y css, con iconos y elementos SVG embebido dentro del propio documento html.

Tambien tenemos incrustado la libreria knockout.js mediante enlaces CDN.


comandos para lanzar la api rest
~~~

uvicorn app.main:app --reload

Set-Location .\backend
python -m uvicorn app.main:app --reload

# para instalar las dependenciad del proyecto
python -m pip install -r .\backend\requirements.txt

# instalar entorno virtual
python -m venv .env
.\.env\Scripts\Activate.ps1

#si falla por politica de ejecucion:
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned

Para salir: deactivate

~~~

