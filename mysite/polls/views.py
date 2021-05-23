from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import Question


def index(request):

    latest_question_list = Question.objects.order_by('-pub_date')[:5]

    return render(
        request,
        "polls/index.html",
        {'latest': latest_question_list}
    )

def detail(request, question_id):
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Strona nie istnieje")

    question = get_object_or_404(Question, pk=question_id)
    return render(
        request,
        "polls/detail.html",
        {"question": question}
    )

def results(request, question_id):
    return render(
        request,
        "polls/results.html",
        {}
    )

def vote(request, question_id):
    return render(
        request,
        "polls/vote.html",
        {}
    )

