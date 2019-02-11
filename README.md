
[![Build Status](https://travis-ci.org/TedOnyango/Politico.svg?branch=development)](https://travis-ci.org/TedOnyango/Politico)
[![Coverage Status](https://coveralls.io/repos/github/TedOnyango/Politico/badge.svg)](https://coveralls.io/github/TedOnyango/Politico)

**Politico**
 Politico is an electoral software that with various features as shown below.

*Features*:
- Users can sign up and login
- Admin can create political parties
- Admin can create gvt offices
- Politicians can express post they want to vie in
- Users can vote
- Admin can edit / delete political parties.

Setup and installation
Set up virtualenv

     virtualenv venv
Activate virtualenv

     source venv/bin/activate
Install dependencies

     pip install -r requirements.txt
Setup env variables
ON linux:
$ export FLASK_APP=run.py
$ export FLASK_DEBUG=1
$ export FLASK_ENV=development
Running tests
 On windowss:
 $ set FLASK_APP=run.py
$ set FLASK_DEBUG=1
$ set FLASK_ENV=development
Running tests
 

   python -m pytest --cov=app/api
Start the server

   flask run

**Author:**
Teddy Onyango

**Credits:**
Andela Kenya

** Politico**
Politico is an electoral software that with various features as shown below.

*Features*:
- Users can sign up and login
- Admin can create political parties
- Admin can create gvt offices
- Politicians can express post they want to vie in
- Users can vote
- Admin can edit / delete political parties.


**Author:**
Teddy Onyango

**Credits:**
Andela Kenya
