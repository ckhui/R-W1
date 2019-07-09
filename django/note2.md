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