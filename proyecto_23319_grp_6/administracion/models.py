from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
    
class Persona(models.Model):
    """MODELO QUE PERMITE DEL USER MODEL DE DJANGO PARA AGREGERLE CAMPOS EXTRAS"""
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    email = models.EmailField(max_length=100,verbose_name='Email')
    telefono = models.CharField(max_length=50,verbose_name='Telefono')
    provincia = models.CharField(max_length=50,verbose_name='Provincia')
    calle = models.CharField(max_length=100,verbose_name='Calle')
    codigo_postal = models.CharField(max_length=10,verbose_name='CodigoPostal')
    fecha_alta =  models.DateField(auto_now_add=True,verbose_name='Fecha de alta')
    foto = models.ImageField(upload_to='perfiles/',null=True,verbose_name='Foto Perfil')
    
    def __str__(self):
        return f"{User.username}"
    
    #def soft_delete(self):
    #    self.baja=True
    #    super().save()
    
    
    class Meta():
        verbose_name_plural = 'Personas'
        
class Clasificacion(models.Model):
    desc_clasificacion = models.CharField(max_length=100,verbose_name='Clasificacion')
    fecha_alta =  models.DateField(auto_now_add=True,verbose_name='Fecha de alta')
    
    def __str__(self):
        return f"{self.desc_clasificacion}"
    
    class Meta():
        verbose_name_plural = 'Clasificaciones'
        
        
class Producto(models.Model):
     
    ESTADOS = [
        ('A','Activo'),
        ('I','Inactivo'),
        ('P','Pausado'),
    ]
    desc_producto = models.CharField(max_length=100,verbose_name='Descripcion Producto')
    estado = models.CharField(choices=ESTADOS,default='A', max_length=1)
    clasificacion = models.ForeignKey(Clasificacion,on_delete=models.CASCADE)
    persona = models.ForeignKey(Persona,on_delete=models.CASCADE)
    fecha_alta = models.DateField(auto_now_add=True,verbose_name='Fecha de alta')
    foto  = models.ImageField(upload_to='image/',null=True,verbose_name='Foto Producto')
    precio = models.PositiveIntegerField(verbose_name='Precio',null=True)
    titulo= models.CharField(max_length=100,verbose_name='Titulo',null=True)
    def __str__(self):
        return f"{self.desc_producto}"
    
    class Meta():
        verbose_name_plural = 'Productos'
        
class Cab_Compras(models.Model):
    comprador = models.ForeignKey(Persona,on_delete=models.CASCADE)
    fecha_compra = models.DateField(auto_now_add=True,verbose_name='Fecha de alta')
    
class Det_Compras(models.Model):
    producto = models.ForeignKey(Producto,on_delete=models.CASCADE)
    precio = models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Precio')
    cantidad = models.IntegerField(verbose_name='Cantidad')