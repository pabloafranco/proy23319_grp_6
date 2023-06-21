import pdb

from typing import Any, Dict
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


from administracion.models import Producto, Clasificacion
from .forms import ProductoForm
# Create your views here.


from . import views

# Create your views here.
def home(request):
    return render (request,'publica/home/home.html')

def login_view(request):
    #Si el usuario ya esta autenticado no lo dejo entrar
    if request.user.is_authenticated:
        return redirect('detailProduct')
    
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
    
    listado_productos = Producto.objects.all()
    
    method='paso por get'
    titulo='Pagina de detalle de productos'
    fecha=datetime.now
    return render(request,'publica/home/products.html',{
        'titulo':titulo,
        'fecha':fecha,
        'method':method,
        'productos':listado_productos
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
    
    #Si el usuario ya esta autenticado no lo dejo entrar
    if request.user.is_authenticated:
        return redirect('detailProduct')
        
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
        
        print(f'request: {request}')
        user=form.save() #Llamamos al save de la clase!
        if user:
            #login(request,user)
            messages.success(request,'Usuario creado exitosamente')
            login(request,user)
            
            
#            formulario = Registrarform(request.POST or None,request.FILES or None) #
            
            ## Le asigo el codigo del usuario autenticado!
 #           formulario.user_id = request.user.id
  #          formulario.save()
            #Hago la grabacion del usuario
            
            
            return redirect('detailProduct')
    
    return render(request, 'publica/login/formlogin.html', { 
                            'form': form,
    })        
    
def logout_view(request):
    logout(request)
    messages.success(request, "Sesion cerrada existosamente")
    return redirect('login')
    
    

def productos_index(request):
    productos = Producto.objects.all()
    return render(request,'publica/productos/index.html',{'productos':productos})    

def productos_nuevo(request):
    #pdb.set_trace() ## Punto de ruptura
    if(request.method=='POST'):
        #user=User.objects.get(pk=1)
        # formulario = ProductoForm(request.POST or None,request.FILES or None, instance=user) #
        formulario = ProductoForm(request.POST or None,request.FILES or None) #
        
        if formulario.is_valid():
            form = formulario.save(commit=False)
            
            ## Le asigo el codigo del usuario autenticado!
            form.persona_id = request.user.id
            form.save()
            return redirect('productos_index')
        else:
            messages.success(request,'NO PASO LA VALIDACION')
    else:
        formulario = ProductoForm()
    return render(request,'publica/productos/nuevo.html',{'formulario':formulario})

def productos_editar(request,id):
    try:
        producto = Producto.objects.get(pk=id)
    except Producto.DoesNotExist:
        return render(request,'publica/productos//404_admin.html')

    if(request.method=='POST'):
        formulario = ProductoForm(request.POST,instance=producto)
        if formulario.is_valid():
            formulario.save()
            return redirect('productos_index')
    else:
        formulario = ProductoForm(instance=producto)
    return render(request,'publica/productos/editar.html',{'formulario':formulario})

def productos_eliminar(request,id_producto):
    try:
        producto = Producto.objects.get(pk=id)
    except Producto.DoesNotExist:
        return render(request,'publica/productos//404_admin.html')
    producto.delete()
    return redirect('productos_index')
    
    
    
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from administracion.models import Clasificacion
from django.http import HttpResponseRedirect

from django.shortcuts import get_object_or_404
from django.contrib import messages

from administracion.forms import ClasificacionForm
# Create your views here.
def index_administracion(request):
    variable = 'test variable'
    return render(request,'administracion/index_administracion.html',{'variable':variable})



"""
    IMPLEMENTACION DE CRUD DE Clasificacion POR MEDIO DE VISTAS BASADAS EN CLASES (VBC)
"""
class ClasificacionListView(ListView):
    model = Clasificacion
    context_object_name = 'Clasificacion'
    template_name= 'publica/Clasificaciones/index.html'
    queryset= Clasificacion.objects.all()
    ordering = ['desc_clasificacion']
    
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['message'] = "Listado de clasificaciones"
        context['clasificaciones'] = context['object_list']
        return context

class ClasificacionCreateView(CreateView):
    model = Clasificacion
    # fields = ['nombre']
    form_class = ClasificacionForm
    template_name = 'publica/Clasificaciones/nuevo.html'
    success_url = reverse_lazy('clasificaciones_index_view')
    
    # def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
    #     context = super().get_context_data(**kwargs)
    #     print(context)
    #     context['message'] = "Listado de clasificaciones"
    #     context['clasificaciones'] = context['object_list']
    #     return context

class ClasificacionUpdateView(UpdateView):
    model = Clasificacion
    fields = ['desc_clasificacion']
    # form_class = ClasificacionForm
    template_name = 'publica/Clasificaciones/editar.html'
    success_url = reverse_lazy('clasificaciones_index_view')

    def get_object(self, queryset=None):
        pk = self.kwargs.get(self.pk_url_kwarg)
        obj = get_object_or_404(Clasificacion, pk=pk)
        return obj
    
class ClasificacionDeleteView(DeleteView):
    model = Clasificacion
    template_name = 'publica/Clasificaciones/eliminar.html'
    success_url = reverse_lazy('clasificaciones_index_view')
    
    def get_object(self, queryset=None):
        pk = self.kwargs.get(self.pk_url_kwarg)
        obj = get_object_or_404(Clasificacion, pk=pk)
        return obj
    
    #se puede sobreescribir el metodo delete por defecto de la VBC, para que no se realice una baja fisica
    """  def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.soft_delete()  # Llamada al método soft_delete() del modelo
        return HttpResponseRedirect(self.get_success_url()) """
    
    