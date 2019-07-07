from django.urls import path

from .views import (
    IndexView,
    DetailView,
    ResultsView,
    vote,
)
app_name = 'polls'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    # ex: /polls/5/
    path('<int:pk>/', DetailView.as_view(), name='detail'),
    # ex: /polls/5/results/
    path('<int:pk>/results/', ResultsView, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', vote, name='vote')

]
