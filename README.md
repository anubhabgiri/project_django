# project django

## Getting started

To create a Django project

` django-admin startproject <project name> <folder name>`

To start server

` python manage.py runserver`

To create app in Django project

` python manage.py startapp <app name>`

Note: installed apps must be added to settings.py/installed apps for Django to recognize them

To migrate the model definitions to the database

`  python manage.py makemigrations <app name> ` This will create the migration files e.g., 0001_initial.py

` python manage.py sqlmigrate <app name> 0001` This will actually prepare the SQL statements

` python manage.py migrate` This will execute the statements


## Super user creds

uname: anubh  
email: anubhabgiri@gmail.com  
pwd: password