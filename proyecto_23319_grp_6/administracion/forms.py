from django import forms

from administracion.models import Clasificacion

class ClasificacionForm(forms.ModelForm):
    # nombre = forms.CharField(error_messages={'required':'Hello! no te olvide de mi!'})

    class Meta:
        model=Clasificacion
        # fields='__all__'
        fields=['desc_clasificacion']
        #exclude=('baja',)
        widgets = {
            'desc_clasificacion' : forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese una Clasificacion'})
        }
        error_messages = {
            'nombre' :{
                'required':'No te olvides de mi!'
            }
        }
