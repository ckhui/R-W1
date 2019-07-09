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