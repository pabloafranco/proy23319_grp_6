from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from . import views

# Create your views here.
def home(request):
    return render (request,'publica/home/home.html')
def login(request):

    return render (request,'publica/login/login.html')
def formLogin(request):

    return render (request,'publica/login/formLogin.html')
# con parametro en la uri
def homeLogIn(request, idUser):
    return HttpResponse(f"""Proyecto <h1>Django Home  Login {idUser} <h1>""")
# con metodo get
def detailProduct(request):
    method='paso por get'
    titulo='pagina de detalle de productos'
    fecha=datetime.now
    return render(request,'publica/home/products.html',{
        'titulo':titulo,
        'fecha':fecha,
        'method':method
    })
# con metodo post
# def saveUser(request):
#     return HttpResponse(f"""Proyecto <h1>Django pruducto detalle  <h1>""")

