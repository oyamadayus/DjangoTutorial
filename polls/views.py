from django.shortcuts import render
from django.http import HttpResponse
import datetime
from django.utils import timezone


def index(request):
    return HttpResponse(f"Hello, world. You're at the polls index. datetime.now:{datetime.datetime.now()}, {timezone.now()}")
# Create your views here.
