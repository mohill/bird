Overview
========

This is a bird application. It stores and fetches birds in a Mongo-database.
It's entirely written in Python with the Flask framework.

The code has only been tested with Python 2.7 on Linux.

Index
=====
 * Requirements
 * Installation
 * MongoDB
 * Running
 * Permanent installation
 * Testing

Requirements
============
The application is tested on the versions within ().

Languange: 
 * Python (2.7)

Modules:
 * Flask (0.10.1)
 * PyMongo (3.0.2)
 * Flask-Testing (0.4.2)

 Database:
 * MongoDB (3.0.4)

Installation
============
Install Python 2.7 and pip with recommended dependencies.
$ apt-get update

$ apt-get install python-pip

$ pip install pymongo flask Flask-Testing

MongoDB
=======
A default installation of MongoDB with a password-less connection is expected.

$ apt-get install mongodb

Running
=======
It simply starts with 
$ python app.py

It runs and listens on http://0.0.0.0:8000

Permanent installation
======================
If the application is to be permanently installed it is recommended to run 
on with Nginx and Gunicorn in a virtual environment as a WSGI application.

Testing
=======
test.py uses Flask unittest to ensure functionality of the application.
It runs 5 simple tests to ensure that we get a HTTP 200 OK from the application.

It requires one bird in the database on first run not to produce any errors.
After first run, take the object-id of that bird and add it to the variable:
existing_bird_id_url = "/birds/559979dc25d367210c295fef"

Simply run it with
$ python test.py