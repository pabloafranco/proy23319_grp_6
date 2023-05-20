from django import forms

from .models import Clasificacion

class CategoriaForm(forms.ModelForm):
    # nombre = forms.CharField(error_messages={'required':'Hello! no te olvide de mi!'})

    class Meta:
        model=Categoria
        # fields='__all__'
        fields=['nombre']
        #exclude=('baja',)
        widgets = {
            'nombre' : forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese un nombre'})
        }
        error_messages = {
            'nombre' :{
                'required':'No te olvides de mi!'
            }
        }
