validator
=========
Small web application for validating ocds data

Requirements
============
Installation has been tested on an ubuntu machine. You will need:
* pip
* MySQL


Install
=======
The whole application runs inside a virtualenv, but you do not have to manage
it yourself, the [dye](https://github.com/aptivate/dye) commands handle this for you.

After cloning the repo, go to the deploy directory:

    $ cd validator/validator/deploy

The bootstrap.py command sets up a virtualenv for us:

    $ ./bootstrap.py

Now we use the deploy command to do the following:
* sets up our sql database for the first time including creating a new username
  and password (this is why deploy wants your mysql root password)
* links to the correct local settings files
* does other deploy things (which are generally more relevant when deploying to
  server - building webassets etc.

    $ ./tasks.py deploy:dev

Run validator locally
=====================
Go into the django directory and use manage.py to run django:

    $ ./manage.py runserver

./manage.py automatically runs validator inside the virtualenv that was setup
by bootstrap.py

Run tests
=========
py.test and pytest-django are used for testing validator. To run the tests use:

    $ ./manage.py test

This automatically invokes pytest and you can pass all pytest arguments e.g.:

    $ ./manage.py test --fixtures

Adding new requirements
=======================
To add new pip packages to validator, add them to deploy/pip_packages.txt.
After doing this, run bootstrap.py again to update your virtualenv.
