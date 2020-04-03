# create-flask-service
Set up a Flask microservice with a few keystrokes

## 👶 Dependencies
* [Python 3.6 or higher](https://www.python.org/downloads/)
* [Git SCM](https://git-scm.com/downloads)

## 🛠️ Installation
Install from PyPI using `pip`
```bash
$ pip install create-flask-service
```

## 🚀 Usage
![Demo](https://github.com/amickael/create-flask-service/blob/master/animation.svg)
TBD

## 📦 What's in the box
### Boilerplate directory structure. Adapted from [a guide by AJ Pryor](http://alanpryorjr.com/2019-05-20-flask-api-example/), author of the excellent [flask_accepts](https://github.com/apryor6/flask_accepts) library (included)
```
.
├── README.md
├── __init__.py
├── app.py
├── controller
│   └── __init__.py
├── database
│   └── __init__.py
├── interface
│   └── __init__.py
├── model
│   └── __init__.py
├── requirements.txt
├── schema
│   └── __init__.py
├── scripts
│   └── __init__.py
├── service
│   └── __init__.py
└── utils
    └── __init__.py
```

### Python virtual environment with the following libraries installed, remember to activate the environment before developing
* [flask](https://github.com/pallets/flask) - The Python micro framework for building web applications
* [flask-restx](https://github.com/python-restx/flask-restx) - Fully featured framework for fast, easy and documented API development with Flask
* [flask_accepts](https://github.com/apryor6/flask_accepts) - Easy, opinionated Flask input/output handling mixing Marshmallow with flask-restx
* [flask-compress](https://github.com/colour-science/flask-compress) - Compress responses in your Flask app with gzip
* [flask-cors](https://github.com/corydolphin/flask-cors) - Cross Origin Resource Sharing ( CORS ) support for Flask
* [python-dotenv](https://github.com/theskumar/python-dotenv) - Get and set values in your .env file in local and production servers
* [marshmallow](https://github.com/marshmallow-code/marshmallow) - A lightweight library for converting complex objects to and from simple Python datatypes
* [python-jose](https://github.com/mpdavis/python-jose) - A JOSE implementation in Python
* [werkzeug](https://github.com/pallets/werkzeug) - The comprehensive WSGI web application library
* [flask-sqlalchemy](https://github.com/pallets/flask-sqlalchemy) - The Database Toolkit for Python
* [pyodbc](https://github.com/mkleehammer/pyodbc) - Python ODBC bridge
* [typing-extensions](https://github.com/python/typing/tree/master/typing_extensions)
  * Note that this is only needed for Python <3.7
### Initialized git repository with a Python-specific .gitignore file
* Nothing will be committed automatically

### Basic README.md file
