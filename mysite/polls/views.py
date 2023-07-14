# Create your views here.
from typing import Any
from django.db.models.query import QuerySet
from django.http import HttpResponse, HttpResponseRedirect
#from django.template import loader
#from django.shortcuts import render
from .models import Choice, Question
from django.urls import reverse
#raising a 404 error
from django.shortcuts import get_object_or_404, render
from django.views import generic
#Question “index” page – displays the latest few questions.
class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """Return the last five published questions:"""
        return Question.objects.order_by("-pub_date")[:5]
class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"
class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"
# def index(request):
#     #return HttpResponse("Hello, My Name is Usama Bin basharat")
#     latest_question_list = Question.objects.order_by("-pub_date")[:5]
#     #output = ", ".join([q.question_text for q in latest_question_list])
#     #template = loader.get_template("polls/index.html")
#     context = {
#         "latest_question_list": latest_question_list,
#     }
#     return render(request, "polls/index.html" , context)


# Leave the rest of the views (detail, results, vote) unchanged
#Question “detail” page – displays a question text, with 
#no results but with a form to vote.
# def detail(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, "polls/detail.html", {"question": question})
#Question “results” page – displays results for a particular question.
# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     #response = "You're looking at the results of question %s."
#     return render(request, "polls/results.html", {"question": question})
#Vote action – handles voting for a particular choice in a
#particular question.

    
#
def vote_reset(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    for choice in question.choice_set.all():
        choice.votes = 0
        choice.save()

    return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))        

def add_question(request):
    if request.method == 'GET':
        return render(request, "polls/new_question.html", {})
        #return a template where we add new question
        
    elif request.method == 'POST':
        #save a new question and go to next page
        user_submitted_question = request.POST["question"]
        if not user_submitted_question:
            #question = get_object_or_404(Question, pk=question_id)
            return render(request, "polls/index.html", {
                "error_message": "Please enter a valid question"
            })






def choice(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.method == 'GET':
        
        return render(request, "polls/choice.html", {"question": question})
    elif request.method == 'POST':
        user_submitted_choice = request.POST["choice"]
        if not user_submitted_choice:
            #question = get_object_or_404(Question, pk=question_id)
            return render(request, "polls/choice.html", {
                "question": question,
                "error_message": "Please enter a valid choice"
            })
            #return HttpResponse("Please enter a valid choice")
        new_choice = Choice(
            question = question,
            choice_text=user_submitted_choice,
        )
        new_choice.save()
        return HttpResponseRedirect(reverse("polls:detail", args=(question.id,)))
        #return HttpResponse("You didnot make a GET response!")


    




def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You did'nt select a choice.",
            },
        )
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))


    #return HttpResponse("You're voting on question %s." % question_id)
