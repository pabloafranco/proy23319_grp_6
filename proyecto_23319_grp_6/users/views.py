from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect
from django.conf import settings

from django.core.mail import send_mail

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

    return redirect('detailProduct')         