from django.contrib import messages
from django.shortcuts import redirect
from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from publica.forms import VenderProductoform
from publica.forms import Ingresarform
from publica.forms import Registrarform

from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth import authenticate

from django.contrib.auth.models import User

from . import views

# Create your views here.
def home(request):
    return render (request,'publica/home/home.html')

def login_view(request):
    if request.method=="POST":
        username = request.POST.get('username')  #POST es un diccionario
        password = request.POST.get('password')  # Si no encuentra valor retorna None, con '', se puede poner un valor por default
        #print(username)
        #print(password)
        
        #Verifico si existe el usuario
        user= authenticate(username=username, password=password)
        if user:
            # Le genero una sesion al usuario
            login(request, user)
            messages.success(request,"Bienvenido {}".format(username))
            return redirect('detailProduct')
        else:
            messages.error(request,"Usuario o contraseña no validos")
            
            
        
    
    return render (request,'publica/login/login.html', {})


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
"""
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
"""        
def formLogin(request):    
    
    #if request.user.is_authenticated:
    #    return redirect('index')
    
    form = Registrarform(request.POST or None)
    
    if request.method=='POST' and form.is_valid():
        
        username=form.cleaned_data.get('username')
        email=form.cleaned_data.get('email')
        tipo_usuario = form.cleaned_data.get('tipousuario')
        password=form.cleaned_data.get('password')
        password2=form.cleaned_data.get('password2')
        direccion1=form.cleaned_data.get('direccion1')
        provincia=form.cleaned_data.get('provincia')
        cp=form.cleaned_data.get('cp')
        
     
        user=form.save() #Llamamos al save de la clase!
        if user:
            #login(request,user)
            messages.success(request,'Usuario creado exitosamente')
            login(request,user)
            return redirect('detailProduct')
    
    return render(request, 'publica/login/formlogin.html', { 
                            'form': form,
    })        
    
def logout_view(request):
    logout(request)
    messages.success(request, "Sesion cerrada existosamente")
    return redirect('login')
    