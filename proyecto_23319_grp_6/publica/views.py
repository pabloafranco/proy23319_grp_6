from django.contrib import messages
from django.shortcuts import redirect
from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from publica.forms import VenderProductoform
from publica.forms import Ingresarform

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
    listado_cursos = [
        {
            'nombre':'NoteBook',
            'descripcion':'I7 - 8gb RAM - Inter',
            'categoria':'Tecnologia',
        },
        {
            'nombre':'Heladera',
            'descripcion':'NoFrost',
            'categoria':'Electrodomesticos',
        },
        {
            'nombre':'TV Smart LED',
            'descripcion':'4K Philips',
            'categoria':'Tecnologia',
        },
        {
            'nombre':'Parlante WiFi',
            'descripcion':'Parlante Sony',
            'categoria':'Tecnologia',
        },
    ]
    method='paso por get'
    titulo='Pagina de detalle de productos'
    fecha=datetime.now
    return render(request,'publica/home/products.html',{
        'titulo':titulo,
        'fecha':fecha,
        'method':method,
        'cursos':listado_cursos
    })
# con metodo post
# def saveUser(request):
#     return HttpResponse(f"""Proyecto <h1>Django pruducto detalle  <h1>""")


def venderView(request):    
    
    #if request.user.is_authenticated:
    #    return redirect('index')
    
    form = VenderProductoform(request.POST or None)
    
    if request.method=='POST' and form.is_valid():
        
        
        #user = form.save()
        user="OK"
        
        if user:
            #login(request,user)
            messages.success(request,'Producto creado exitosamente')
            return redirect('detailProduct')
    
    return render(request, 'publica/home/vender.html', { 
                            'form': form,
    })
    
def ingresarView(request):    
    
    #if request.user.is_authenticated:
    #    return redirect('index')
    
    form = Ingresarform(request.POST or None)
    
    if request.method=='POST' and form.is_valid():
        
        
        #user = form.save()
        user="OK"
        
        if user:
            #login(request,user)
            messages.success(request,'Usuario creado exitosamente')
            return redirect('detailProduct')
    
    return render(request, 'publica/home/login.html', { 
                            'form': form,
    })    