# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
#from django.template import loader
#from django.shortcuts import render
from .models import Choice, Question
from django.urls import reverse
#raising a 404 error
from django.shortcuts import get_object_or_404, render
#Question “index” page – displays the latest few questions.
def index(request):
    #return HttpResponse("Hello, My Name is Usama Bin basharat")
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    #output = ", ".join([q.question_text for q in latest_question_list])
    #template = loader.get_template("polls/index.html")
    context = {
        "latest_question_list": latest_question_list,
    }
    return render(request, "polls/index.html" , context)


# Leave the rest of the views (detail, results, vote) unchanged
#Question “detail” page – displays a question text, with 
#no results but with a form to vote.
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})
#Question “results” page – displays results for a particular question.
def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    #response = "You're looking at the results of question %s."
    return render(request, "polls/results.html", {"question": question})
#Vote action – handles voting for a particular choice in a
#particular question.

    
def choice(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        choice_to_add = request.POST["new_choice"]
        if not choice_to_add:
            raise KeyError
    except(KeyError):
         return render(
            request,
            "polls/choice.html",
            {
                "question": question,
                "error_message": "The choice could not be added.",
            },
        )
    else:
        newChoice=Choice(
            question=question,
            choice_text= choice_to_add
        )
        newChoice.save()
        return HttpResponseRedirect(reverse("polls:detail", args=(question.id,)))

    




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
