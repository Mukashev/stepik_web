from django.shortcuts import render
from django.http import HttpResponse 

# Create your views here.

def test(request, *args, **kwargs):
    return HttpResponse('OK')

def login(request, *args, **kwargs):
    pass

def signup(request, *args, **kwargs):
    pass

def ask(request, *args, **kwargs):
    pass

def popular(request, *args, **kwargs):
    pass

def new(request, *args, **kwargs):
    pass