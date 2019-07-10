# Django Tutorial 4++
[link](https://docs.djangoproject.com/en/2.2/intro/tutorial04/)

## Writing a simple form
- radio button for each options
- will POST data **choice=#** where # is the ID of selected choice.
- when doing POST request
    - can have the effect of modifying data
    - need to worry about CSRT (cross Site Request Forgeries)
    - Django: all POST form that are targeted at internal URL need to use {% scrf_token%} tag

## Handle POST request
- HttpResponseRedirect instead of HttpResponse after POST request (best practice)
- to avoid go back and cause another submission

### reverse()
- to avoid hardcoded url and using reference similar to {% url %} tag
- reverse('polls:results', args=(question.id,))
- '/polls/3/results/'

### Race Condition
- when 2 user vote at the same time, and update the database count
- will cause database to store the last value but not the expected value
- (Avoiding race conditions using F())[https://docs.djangoproject.com/en/2.2/ref/models/expressions/#avoiding-race-conditions-using-f]
- instead of doing read and update to DB
- ask the database to do the update


## Use Generic Views
### Amend URLconf
- change **<question_id>** to **<pk>**

### Amend View
- from django.views import generic
- ListView and DetailView
- each generic view need to know
    - model
        - set the "model" variable
    - DetailView: expects primary key value capture by the url to be **"pk"**
        - thats why chaning the url.py to use "pk"
    - template
        - default: <appName>/<modelNamr>_detail.html
        - can set the "template_name" variable
    - context
        - default context will be "question_list"
        - but our template is build for "latest_question_list"
        - can change it by setting "context_object_name"

## TEST
- test are simple routines that check the operation of your code
- Why
    - save time
        - when the app becomes conplex
    - prevent problems
    - more attractive code
    - help teams work together
- TDD, test-driven development

## Create test
- add to tests.py
- run test
> python manage.py test polls

## Test View
- Django provides a test **Client** to simulate a user interaction with the code at the view level
- can use in **tests.py** or **shell**

> from django.test.utils import setup_test_environment
> setup_test_environment()
    - installs a template renderer
    - allow to examine some additional attributes
        - response.contest
    - does not setup a test DB
    - everything will be run against the existing DB

> from django.test import Client
> client = Client()
- client to do sth 
> response = client.get('/')

### Comparision 
 - assertContains()
 > self.assertContains(response, "No polls are available.")
 - assertQuerysetEqual()
 > self.assertQuerysetEqual(response.context['latest_question_list'],  ['<Question: Past question 2.>', '<Question: Past question 1.>'])
 - 404
 > self.assertEqual(response.status_code, 404)


## rules-of-thumb
- separate TestClass for each model or view
- separate test method for each set of conditions you want to test
- test method names that describe their function

## Further testing
- test framework "(Selenium)[https://www.seleniumhq.org/]" to test whether HTML actually being rendered
- testing javascript
- Django: LiveServerTestCase
- run tests actumatically for every commit: CI (continuous integration)
- check code coverage
- 


## Static file
- some non generated file need to be served together with the HTML
- eg. images, javascript or css 
- **django.contrib.staticfiles** will collects all the static files into a single location to be served in production
- need to create a folder "static" in the app
- create another "polls" folder inside (for namespacing)
- structure: polls/static/polls/style.css
- to use
 - **{% load static %}** in template file
 - **{% static %}** tag to get absolute URL of static file
    - href="{% static 'polls/style.css' %}"

## Customize the admin form
- edit admin.py
```python
#[default]
admin.site.register(Question)
```
- change to 
```python
class QuestionAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'question_text']

admin.site.register(Question, QuestionAdmin)
```

when want to change the admin options for a model
- create a model admin class
- pass in as 2nd arg for admin.site.register()

- can use fieldsets
    - seperate to sessions

### Adding Related Object
- Question will have mulitple Choice

- Django know that a **ForeignKey** should be represented as a **<select>** box.
- But now, you can add a Choice when editing Question

- 'classes': ['collapse']
    - to allow fieldsets to be hide/show
- admin.StackedInline
    - stack for input
- admin.TabularInline
    - input in table form ( save space)

- list_display
    - to set what info to display, on index page (before edit)
    - change the column name and order
    - make the change in to model
        - field.admin_order_field = 'pub_date'
        - field.boolean = True
        - field.short_description = 'Published recently?'
- list_filter
    - add a filter by the field to sidebar
- search_fields
    - add a search bar, and will search for the filed
- paggination, search box, filters, date-horerarchies, column-header-ordering
    - refer to doc