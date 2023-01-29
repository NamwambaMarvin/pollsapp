from django.urls import path
from . import views2
#namespace just incase of many apps 
app_name = 'polls'
#used by the {% url %} name tag to specify the app
'''urlpatterns = [
    #ex polls
    path('',views.index,name='index'),
    #ex polls/34
    path('<int:question_id>/',views.details,name='details'),
    path('<int:question_id>/results',views.results,name='results'),
    path('<int:question_id>/vote',views.vote,name='vote')
]'''
urlpatterns = [ 
    path('', views2.IndexView.as_view(), name='index'), 
    path('<int:pk>/', views2.DetailView.as_view(), name='details'), 
    path('<int:pk>/results/', views2.ResultsView.as_view(), name='results'), 
    path('<int:question_id>/vote/', views2.vote, name='vote'), 
    ]
