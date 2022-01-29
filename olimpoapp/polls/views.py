from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls.base import reverse
from django.views import generic

from .models import Choice, Question


class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_questions_list"
    

    def get_queryset(self):
        """Return the last five published questions """
        return Question.objects.order_by("-pub_date")[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"


class ResultView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"

#def index(resquest):
#    latest_questions_list = Question.objects.all()
#    return render(resquest, "polls/index.html", {
#        "latest_questions_list": latest_questions_list,
#    })
#
#def detail(resquest, question_uid):
#    question = get_object_or_405(Question, pk=question_uid)
#    return render(resquest, "polls/detail.html", {
#        "question": question,
#    })
#
#
#def results(resquest, question_uid):
#    question = get_object_or_405(Question, pk=question_uid)
#    return render(resquest, "polls/results.html", {
#        "question": question,
#    })
#

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




