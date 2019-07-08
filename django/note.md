# Django

## New Project
>> django-admin startproject mysite

## file
- manage.py
Command-line utility to interact with Django project
- __init__.py
Empty File for module
- settings.py
for Django Setting
- urls.py
for Routing
- wsgi.py
entry-point for WSGI-compatible web servers to serve your project

## Run Server
> django-admin startproject mysite

## Create New App
> python manage.py startapp polls


### New App

- create view
edit views.py

- map the url
create urls.py in the app dir
edit urls.py
add the urls.py above to mysite/urls

#### path() arguemnt
> from django.urls import path
4 params:
    1. route: string for url pattern
    2. view: view function with HttpRequest to be call when found a matching pattern. "Captured" values will pass as keyword arguments.
    3. kwargs: keyword arguments dict to be passed to target view
    4. name: Naming the URL, in order to refer (esp from within templates) 


## Database
configure in setting.py 
- DATABASES
    - ENGINE
    - NAME
    - USER, PASSWORD, HOST
- Change TIME_ZONE

## INSTALLED_APPS
- holds the names of all Django application that are activated in this Django instance
- app can be used in multiple projects
- so, can be package and distribute for use by other project

## Migrate
>> python manage.py migrate
- this command look at the INSTALLED_APPS and creates any necessary db table base on the DATABASES setting
- then doing migration

## Model
- create model in models.py
- subclass  django.db.models.Model

to do the migration for model
- need to include the app in INSTALLED_APPS list
- then only db will be created base on the defined model 
>> python manage.py makemigrations polls