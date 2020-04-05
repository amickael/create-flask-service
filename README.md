[![GitHub issues](https://img.shields.io/github/issues/amickael/create-flask-service)](https://github.com/amickael/create-flask-service/issues)
![PyPI](https://img.shields.io/pypi/v/create-flask-service?color=blue)
![PyPI - Downloads](https://img.shields.io/pypi/dw/create-flask-service?color=red)
[![GitHub license](https://img.shields.io/github/license/amickael/create-flask-service?color=purple)](https://github.com/amickael/create-flask-service/blob/master/LICENSE)
[![Code style](https://img.shields.io/badge/code%20style-black-black)](https://github.com/psf/black)

# create-flask-service
Set up a Flask microservice with a few keystrokes

## 👶 Dependencies
* [Python 3.6 or higher](https://www.python.org/downloads/)
* [Git SCM](https://git-scm.com/downloads)

## 🛠️ Installation
Install from PyPI using `pip`, you may need to use `pip3` depending on your installation
```bash
$ pip install create-flask-service
```

## 🚀 Usage
![Demo](https://github.com/amickael/create-flask-service/blob/master/demo.gif)

1. Run the `create-flask-service` command
2. Enter your new project name, note that spaces will be converted to dashes
3. Enter the root directory for your new project, if none is supplied then the current directory is used
4. Watch the magic happen

To start the application run `app.py` and navigate to http://127.0.0.1:5000, you should see a blank Swagger UI page. Note that in certain IDEs like PyCharm you may need to set your working directory to the project root, this will ensure that the .env file is loaded before runtime.

## ⚙️ Command Line Arguments
> Note that supplying arguments will not run the main program

| Name    | Argument | Description                      | Default |
|---------|----------|----------------------------------|---------|
| Version | -V       | Display installed version number | False   |

## 📦 What's in the box
* Boilerplate directory structure. Adapted from [a guide by AJ Pryor](http://alanpryorjr.com/2019-05-20-flask-api-example/), author of the excellent [flask_accepts](https://github.com/apryor6/flask_accepts) library (included)
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

* Python virtual environment with the following libraries installed, remember to activate the environment before developing
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
    * [pytest](https://github.com/pytest-dev/pytest) - The pytest framework makes it easy to write small tests, yet scales to support complex functional testing
    * [typing-extensions](https://github.com/python/typing/tree/master/typing_extensions)
      * Note that this is only needed for Python <3.7
* Basic Flask and Flask-RestX configuration
    * app.py contains basic configuration setting up Flask, Flask-SQLAlchemy, CORS, and gzip compression
    * controller/\_\_init\_\_.py contains basic Flask-RestX configuration based on the [Flask-RestX guidelines](https://flask-restx.readthedocs.io/en/latest/scaling.html)
    * Boilerplate code style is formatted with [Black](https://github.com/psf/black), but you may use whatever style suits you
* Initialized git repository with a Python-specific .gitignore file
  * Nothing will be committed automatically
* Basic README.md file

## ⚖️ License
[MIT © 2020 Andrew Mickael](https://github.com/amickael/create-flask-service/blob/master/LICENSE)
