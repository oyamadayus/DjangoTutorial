from django.shortcuts import render
from django.http import HttpResponse
import datetime
from django.utils import timezone


def index(request):
    return HttpResponse(f"Hello, world. You're at the polls index. datetime.now:{datetime.datetime.now()}, {timezone.now()}")

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

# Create your views here.
