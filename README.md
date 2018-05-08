[![License](http://img.shields.io/badge/license-MIT-blue.svg?style=flat-square)](http://opensource.org/licenses/MIT)

# Overview

A starter pack for Python/Flask developers based on good intentions,
module/test driven development and good code quality/structure .
This pack bootstraps most of the infrastructure you will need when
building applications with the flask micro framework at the same time
giving structure to your code and saving you time in setting up.
The starter pack got you cover from your initial commit
to continuously integrating/deploying of your flask app.


# Installation

The application requires the following dependencies:

- Python 2.6 - 3.6
- Docker
- Other dependencies can be installed by the command `pip install -r requirements.txt`

# Starting the application

We strongly recommend using docker to containerize your application but
you don't have to. if you are using docker get started by:

- Updating your app config in config/settings.py using the settings.example.py
sample

- Run ```docker-compose up --build``` to build and
run your docker image
- Access running application on ```http://localhost:5000/```

If you are not using docker:

- Update your app config in config/settings.py using the settings.example.py
sample

- Make sure you have installed all application dependencies by running
`pip install -r requirements.txt`

- Run `gunicorn your_app.app:create_app()`

- Access running application on ```http://localhost:5000/```


# Noted Dependencies

- Gunicorn: HTTP WSGI server for development and production.

- Celery: Task/Queue manager written in Python

- Flask-RESTful: a flask library for building RESTful APIs

- Marshmallow: is an ORM/ODM/framework-agnostic library for converting
complex datatypes, such as objects, to and from native Python datatypes.
We used marshmallow with webargs for serialization/deserialization and also for validation
For more info on Marshmallow click [here](https://marshmallow.readthedocs.io/en/latest/)


- Postgresql: Our bootstrapped starter integrates with PostgreSQL but
you can decide to use any SQL or NoSQl database

- Click: A python library for building custom CLI commands for your
 application for example: db initialization and seeding.
We provided two templates for building cli commands one that accepts arguments
and another options.

# Folder Structure

We used flask blueprint to emphasize modular application development, for
more info on blueprint click [here](http://flask.pocoo.org/docs/1.0/blueprints/)

```
    /cli
    /config
    /your_app
        /blueprints
            /user
                /resources
                /schemas
                /templates
                views.py
    app.py
```

- cli: holds your custom application CLI commands, check out sample for
creating commands with arguments and options

- config: holds application config. see settings.example.py for some of the
application configuration you need to provide. You may decide to hold your
app configs in a .env file.

- your_app: holds app source code arranged in modules using flask blueprint.
Each blueprint has three folders and a views.py file. Explained below

- resources: holds api resources for a blueprint,
 needed especially if you building restful api(s)

- schemas: holds marshmallow schemas for a blueprint

- Templates: holds jinja templates for a blueprint, necessary especially
if you are using flask jinja templating engine for your view layer.

- views.py: This file is where you initialize your blueprint, its resources
and probably its routes

- app.py: create an instance of your application using factory pattern.
This file is where you initialize your blueprints, remember to register
your blueprints else it never happened.

Note: The folder structure is entirely subjective, but scales when
your application gets large. you can have own way of modularizing
your application( It is up to you)



