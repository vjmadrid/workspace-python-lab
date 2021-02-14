# Dependencias del Proyecto


## FLASK

https://pypi.org/project/Flask/

https://flask.palletsprojects.com/en/1.1.x/

Es un framework de desarrollo web para Python

Instalación

```bash
# Instalación
$ pip install -U Flask
```

Variables de entorno

```bash
# FLASK_APP : Indica cual será el fichero que arranca todo (nombre del modulo que se importa como flask run)
export FLASK_APP=helloworld.py # Linux / MacOs
set FLASK_APP=helloworld.py # Windows

# FLASK_ENV : Indica el entorno de ejecución
export FLASK_ENV=development # Linux / MacOs
set FLASK_ENV=development # Windows
```

Uso

```bash
# Ejecuta el arranque a partir de la variable de entorno
flask run

# Ejecuta el arranque partir de la variable de entorno
python -m flask run

# Ejecuta el arranque desde el fichero py
python3 helloworld.py
```

flask run --host=0.0.0.0 --port=80





## Problemas con puertos

```bash
# Detectar proceso en Mac que tiene el puerto bloqueado
sudo lsof -i tcp:5000

# Matar lel proceso informado anteriormente
kill -9 <PID>
```


## Recursos Flask

https://github.com/humiaozuzu/awesome-flask

Flask-SQLAlchemy for database interaction.
Flask-Sessions for user session management.
Flask-Login to manage user logins.
