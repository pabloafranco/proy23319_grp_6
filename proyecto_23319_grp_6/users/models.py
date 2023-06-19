from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

#AbstractUser
class User(AbstractUser):
    email = models.EmailField(max_length=100,verbose_name='Email')
    telefono = models.CharField(max_length=50,verbose_name='Telefono')
    provincia = models.CharField(max_length=50,verbose_name='Provincia')
    calle = models.CharField(max_length=100,verbose_name='Calle')
    codigo_postal = models.CharField(max_length=10,verbose_name='CodigoPostal')
    fecha_alta =  models.DateField(auto_now_add=True,verbose_name='Fecha de alta')
    foto = models.ImageField(upload_to='perfiles/',null=True,verbose_name='Foto Perfil')
    
    def get_full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)

class Customer(User):
    
    class Meta:
        proxy=True  #Hace que no se genere una nueva tabla
        
    def get_products():
        return []
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    
    
# class Persona(models.Model):
#     """MODELO QUE PERMITE DEL USER MODEL DE DJANGO PARA AGREGERLE CAMPOS EXTRAS"""
#     user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
#     email = models.EmailField(max_length=100,verbose_name='Email')
#     telefono = models.CharField(max_length=50,verbose_name='Telefono')
#     provincia = models.CharField(max_length=50,verbose_name='Provincia')
#     calle = models.CharField(max_length=100,verbose_name='Calle')
#     codigo_postal = models.CharField(max_length=10,verbose_name='CodigoPostal')
#     fecha_alta =  models.DateField(auto_now_add=True,verbose_name='Fecha de alta')
#     foto = models.ImageField(upload_to='perfiles/',null=True,verbose_name='Foto Perfil')
    
#     def __str__(self):
#         return f"{self.email}"
    
#     #def soft_delete(self):
#     #    self.baja=True
#     #    super().save()
    
    
#     class Meta():
#         verbose_name_plural = 'Personas'    