# from django.urls import path

# from . import views

# app_name = "polls"
# urlpatterns = [
#     path("", views.index, name="index"),
#     path("<int:pk>/", views.DetailView.as_view(), name="detail"),
#     path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
#     path("<int:question_id>/vote/", views.vote, name="vote"),
# ]""
from django.urls import path

from . import views

app_name = "polls"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
    #/polls/5/choice
    path("<int:question_id>/choice/", views.choice, name="choice"),
    #/polls/5/vote_reset/
    path("<int:question_id>/vote_reset/", views.vote_reset, name="vote_reset"),
    #/polls/5/new/
    path("new/", views.add_question, name="new"),
]