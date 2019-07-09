# Django

# PART1
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


# PART2
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

>> python manage.py check
- check for any problems wihtout making migration or touching the database

>> python manage.py migrate
- to create those model in db
- takes all migrations that haven't been applied

## Make Model Change
- change model (model.py)
- python manage.py makemigrations
- python manage.py migarate

## Shell
> python manage.py shell
- read and manipulate DB 

```
>>> from polls.models import Choice, Question
get all question
>>> Question.objects.all()

create new instance
>>> q = Question(question_text="What's new?", pub_date=timezone.now())

have to call save() explicitly to make change to DB
>>> q.save()

# Access model field values via Python attributes.
>>> q.question_text

# Change values by changing the attributes, then calling save().
>>> q.question_text = "What's up?"
>>> q.save()

>>> Question.objects.all()
```
- filter
- all, count
- get by pk
- create, delete
- accessing related objects
- double underscores for field lookup


Object: <Question: Question object (1)> will not be helpful with id 1
try to modify it by defind __str__(self) in model
- not only convenience when dealing with the interactive prompt
- also object's representations are used for admin


## Admin User
create admin user
> python manage.py createsuperuser

## Make Poll App Modifiable in the admin
register model in admin.py

# PART3

## Add More View
- add view to views.py