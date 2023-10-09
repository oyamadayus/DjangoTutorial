from django.shortcuts import render
from django.http import HttpResponse
import datetime


def index(request):
    return HttpResponse(f"Hello, world. You're at the polls index. Now:{datetime.datetime.now()}")
# Create your views here.
