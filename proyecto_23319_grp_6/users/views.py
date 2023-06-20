from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect
from django.conf import settings

from django.core.mail import send_mail
from administracion.models import Det_Compras, Cab_Compras
from administracion.models import Producto

#from django.contrib.auth.models import User
from users.models import User
# Create your views here.

import environ
import os

    
    
def add(request):
    
    env = environ.Env()
    environ.Env.read_env()

    #cart = get_or_create_cart(request)
    #product = Product.objects.get(pk=request.POST.get('product_id'))
    
    #agregamos un objeto a la relacion
    #cart.products.add(product)
    messages.success(request,'Producto comprado Exitosamente')
    descripcion  = request.POST.get('descripcion')
    email_destino  = request.POST.get('email')
    email_usuario = request.user.email
    print (descripcion)
    print (email_destino)
    print( email_usuario)
    
    mensaje=f"De: {request.user.username}\n Asunto: Compra del producto {descripcion}\n "
    mensaje_html=f"""
            <p>De: {request.user.username} </p>
            <p>Asunto:  Compra del producto {descripcion}</p>
        """
    asunto="COMPRA DEL PRODUCTO - "+descripcion
    
    print(f"EMAIL_HOST_USER: {settings.EMAIL_HOST_USER}")
    print(f"RECIPIENT_ADDRESS: {settings.RECIPIENT_ADDRESS}")
    print(f"EMAIL_HOST_PASSWORD: {settings.EMAIL_HOST_PASSWORD}")
    
    
    send_mail(
        asunto,
        mensaje,
        settings.EMAIL_HOST_USER,
        [settings.RECIPIENT_ADDRESS],
        fail_silently=False,
        html_message=mensaje_html
    )          
    
    """
    class Cab_Compras(models.Model):
    comprador = models.ForeignKey(User,on_delete=models.CASCADE)
    fecha_compra = models.DateField(auto_now_add=True,verbose_name='Fecha de alta')

    class Det_Compras(models.Model):
    cabecera = models.ForeignKey(Cab_Compras,on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto,on_delete=models.CASCADE)
    precioFinal = models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Precio')
    cantidad = models.IntegerField(verbose_name='Cantidad')
    """     
    cabecera = Cab_Compras.objects.create(comprador=request.user)
    cabecera.save()
    id=request.POST.get('id')
    precio=request.POST.get('precio')
    print(f'id: {id}')
    print(f'precio: {precio}')
    
    producto=Producto.objects.get(pk=id)
    detalle = Det_Compras.objects.create(cabecera_id=cabecera.id, cantidad=1, precioFinal=precio, producto=producto)
    #detalle.producto=id
    #detalle.cantidad = 1
    #detalle.precioFinal=precio
    detalle.save()
    

    return redirect('detailProduct')         