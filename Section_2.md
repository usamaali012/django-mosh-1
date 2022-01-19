# SECTION 2

# installing django inside venv
--pipenv install django


# To go into venv
--pipenv shell


# To start project
django-admin startproject <projectname>


# manage.py file is a wrapper around django-admin



# To start server
--python manage.py runserver [portnumber(Optional)]



# TO see the venv directory
--pipenv --venv


# migrations folder in each app for generating database tables.
# admon.py to decide how admin page of our django app will look like
# app.py is place where we configure our app
# models.py is to design model classes for our app and to pull out data from our database
# views.py in NOT used for creating views. It is a RequestHandler for our app. Here we create view functions
# A view function takes a request and returns a response.  REQUEST -> RESPONSE
# urls.py is a file where we map our URLs to our view functions.
# views in django are called templates
# launch.json file is for vscode to know how to debug the appliction
# Middleware in settings.py is used to hook into django's request response processing