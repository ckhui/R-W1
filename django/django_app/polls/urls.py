from . import views
from django.urls import path


app_name = 'polls'
urlpatterns = [
    # ex: /polls/
    ### path('', views.index, name='index'),
    path('', views.IndexView.as_view(), name='index'),

    # ex: /polls/5/
    ###path('<int:question_id>/', views.detail, name='detail'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # similar to calling detail(request=<HttpRequest object>, question_id=5)

    # ex: /polls/5/results/
    ###path('<int:question_id>/results/', views.results, name='results'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),

    # ex: /polls/5/vote/
    ###path('<int:question_id>/vote/', views.vote, name='vote'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]