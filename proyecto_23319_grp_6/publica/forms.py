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

