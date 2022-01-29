from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls.base import reverse

from .models import Choice, Question

def index(resquest):
    latest_questions_list = Question.objects.all()
    return render(resquest, "polls/index.html", {
        "latest_questions_list": latest_questions_list,
    })

def detail(resquest, question_uid):
    question = get_object_or_404(Question, pk=question_uid)
    return render(resquest, "polls/detail.html", {
        "question": question,
    })


def results(resquest, question_uid):
    question = get_object_or_404(Question, pk=question_uid)
    return render(resquest, "polls/results.html", {
        "question": question,
    })


def vote(resquest, question_uid):
    question = get_object_or_404(Question, pk=question_uid)
    try:
        selected_choice = question.choice_set.get(pk=resquest.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        return render(resquest, "polls/detail.html", {
            "question": question,
            "error_message": "No elegiste una opción valida",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,) ))




