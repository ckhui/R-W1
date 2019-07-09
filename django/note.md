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
## config the url
- add view to urls.py

## Custome View and present Templates
- create a folder "templates" in the app dir
- change setting to look for "templates" folder within app
- (setting.py) 'TEMPLATES': 'APP_DIRS': True ## set to True
- File: polls/templates/polls/index.html
- File: APP  /templates/(path to be refer)
- eg: polls/index.html
- ensure namespaing to avoid filename conflict, eg: lots of index.html
### Use Template
- create template folder and file
- configure the setting to look for template folder
- view, get template, get context, present
    - from django.template import loader
    - template = loader.get_template(path)
    - context = {dict})
    - return HttpResponse(template.render(context, request))

- [shortcut]: render()
    - from django.shortcuts import render
    - return render(request, 'polls/index.html', context)


## 404 Page
- from django.http import Http404
- raise Http404("Question does not exist")
or shortcut
- from django.shortcuts import get_object_or_404
- will automatically riase Http404 if no object found
- similar: get_list_or_404()
    - use filter() instead of get() for model
    - raise 404 if list is empty

## Removing Hardcoded URLs in templates
``` html
<li><a href="{% url 'detail' question.id %}">{{ question.question_text }}</a></li>
```
- using {% url 'name defines in urls' param%}
- can just change the url pattern in urls.py and not affecting all the href


## Application Namespace
- to differentiate the URL names between differnce app
- to let Django know whcih app's url to use when using {% url %} tag
- add app_name to urls.py
- including namespace in {% url %} tag
    - "{% url 'detail' question.id %}"
    - "{% url 'polls:detail' question.id %}"