from django import forms
from django.forms import ValidationError
import re

def solo_caracteres(value):
    if any(char.isdigit() for char in value):
        raise ValidationError('El nombre no puede contener números. %(valor)s',
                            code='Invalid',
                            params={'valor':value})

def validate_email(value):
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(email_regex, value):
        raise ValidationError('Correo electrónico inválido')
    return value
 

class VenderProductoform(forms.Form):
    TIPO_PRODUCTO = (
        ('','-Seleccione-'),
        (1,'Electronica'),
        (2,'Electrodomestico'),
        (3,'Muebles'),
    )
    titulo = forms.CharField(
            label='Título', 
            max_length=50,
            widget=forms.TextInput(
                    attrs={'class':'form-control',
                        'placeholder':'Descripcion'}
                    )
        )
    descripcion = forms.CharField(
        label='Descripción',
        max_length=500,
        widget=forms.Textarea(attrs={'rows': 5,'class':'form-control'})
        
    )
    nombreFoto = forms.CharField(
        label='Nombre de la foto',
        max_length=100,
        widget=forms.TextInput( attrs={'class':'form-control',
                        'placeholder':'Descripcion'})
    )
    precio = forms.IntegerField(
        label='Precio'
    )
    tipo_producto = forms.ChoiceField(
        label='Tipo de producto',
        choices=TIPO_PRODUCTO,
        widget=forms.Select(attrs={'class':'form-control'})
    )

    def clean_mensaje(self):
        data = self.cleaned_data['mensaje']
        if len(data) < 10:
            raise ValidationError("Debes especificar mejor el mensaje que nos envias")
        return data

    def clean(self):
        cleaned_data = super().clean()
        asunto = cleaned_data.get("asunto")
        suscripcion = cleaned_data.get("suscripcion")

        if suscripcion and asunto and "suscripcion" not in asunto:
            msg = "Debe agregar la palabara 'suscripcion' al asunto."
            self.add_error('asunto', msg)
            
            
            
class Ingresarform(forms.Form):
    email=forms.EmailField(required=True, 
          widget=forms.EmailInput(attrs={'class': 'form-control',
                                        'id': 'email',
                                        'placeholder': 'example@example.com'}))
   
    password=forms.CharField(required=True, 
          widget=forms.PasswordInput(attrs={'class': 'form-control',
                                            'id': 'password',
                                            'placeholder': 'Password'}))


            
class Registrarform(forms.Form):
    TIPO_USUARIO = (
        ('','-Seleccione-'),
        ('V','Vendedor'),
        ('C','Comprador'),
        ('A','Ambos')
    )
    
    username=forms.CharField(required=True, min_length=4, max_length=50, 
                             label='Usuario', 
                             widget=forms.TextInput(attrs={'class': 'form-control',
                                                           'id': 'username'}))
    email=forms.EmailField(required=True, 
                            label='Email', 
                            widget=forms.EmailInput(attrs={'class': 'form-control',
                                                           'id': 'email',
                                                           'placeholder': 'example@example.com'}))
    tipo_usuario = forms.ChoiceField(
        label='Tipo de usuario',
        choices=TIPO_USUARIO,
        widget=forms.Select(attrs={'class':'form-control'})
    )

    password=forms.CharField(required=True,
                             label='Clave',  
                             widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                           'id': 'password',
                                                           'placeholder': 'Password'}))

    password2=forms.CharField(required=True,
                            label='Repetir clave', 
                            widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                           'id': 'password2',
                                                           'placeholder': 'Password'}))
    direccion1=forms.CharField(required=True, min_length=4, max_length=50, 
                            label='Direccion', 
                            widget=forms.TextInput(attrs={'class': 'form-control',
                                                           'id': 'direccion1'}))

    provincia=forms.CharField(required=False, max_length=50, 
                            label='Provincia', 
                            widget=forms.TextInput(attrs={'class': 'form-control',
                                                           'id': 'provincia'}))

    cp=forms.CharField(required=False, max_length=50, 
                            label='Codigo Potal', 
                            widget=forms.TextInput(attrs={'class': 'form-control',
                                                           'id': 'codigopostal'}))

    def clean_username(self):
        username = self.cleaned_data['username']
        
        #if User.objects.filter(username=username).exists():
        #    raise forms.ValidationError('Username ya se encuentra en uso')
        
        return username
        
    def clean_email(self):
        email = self.cleaned_data['email']
        
       # if User.objects.filter(email=email).exists():
       #     raise forms.ValidationError('Email ya se encuentra en uso')
        
        return email
    
    def clean(self):
        cleaned_data=super().clean()
        
        print (cleaned_data.get('password') )
        print (cleaned_data.get('password2') )
        if cleaned_data.get('password') != self.cleaned_data.get('password2') :
            self.add_error('password2', 'El password no coincide')
                        
    def save(self):
        pass
        #return User.objects.create_user(
        #    self.cleaned_data.get('username'),
        ##    self.cleaned_data.get('email'),
        #    self.cleaned_data.get('password'),
        