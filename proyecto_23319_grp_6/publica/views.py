from django.shortcuts import render
from django.http import HttpResponse
from . import views

# Create your views here.
def hola_mundo(request):
    return HttpResponse('Hola Mundo django')
def index(request):
    return HttpResponse('Proyecto <h1>Django<h1>')