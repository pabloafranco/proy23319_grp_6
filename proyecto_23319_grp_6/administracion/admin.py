from django.contrib import admin

# Register your models here.
from django.contrib import admin
from administracion.models import Persona, Clasificacion, Producto, Cab_Compras,Det_Compras
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin, GroupAdmin

# # Registro por defecto al admin de Django
# admin.site.register(Persona)
# admin.site.register(Clasificacion)
# admin.site.register(Producto)


# Personalizacion de visualizacion de personas
class PersonaAdmin(admin.ModelAdmin):
    list_display_links = ('user',)
    list_display =  ('user','email', 'telefono','provincia','calle','codigo_postal','foto')
    list_editable = ('email', 'telefono','provincia','calle','codigo_postal','foto')
    list_filter = ('provincia', 'codigo_postal')
    search_fields = ('email',)

# Creacion de un Admin Personalizado heredando de AdminSite
class ComprasSite(admin.AdminSite):
    site_header = 'Administracion Mercado Compras'
    site_title = 'Administracion superuser'
    index_title= 'Administracion del sitio'
    empty_value_display = 'No hay datos para visualizar'

class ClasificacionAdmin(admin.ModelAdmin):
    list_display_links = ('desc_clasificacion',)
    list_display =  ('desc_clasificacion',)
    search_fields = ('desc_clasificacion',)

class ProductoAdmin(admin.ModelAdmin):
    list_display_links = ('persona',)
    list_display =  ('desc_producto','estado','clasificacion','persona','foto','precio')
    list_filter = ('estado',)
    search_fields = ('clasificacion',)


# class CategoriaAdmin(admin.ModelAdmin):
#     list_display = ( 'nombre',)
#     exclude = ('baja',)

#     #modificacion del listado que se quiere mostrar
#     def get_queryset(self, request):
#         query = super(CategoriaAdmin, self).get_queryset(request)
#         filtered_query = query.filter(baja=False)
#         return filtered_query

# class CursoAdmin(admin.ModelAdmin):
    
#     #modificar listados de foreingkey
#     def formfield_for_foreignkey(self, db_field, request, **kwargs):
#         if db_field.name == "categoria":
#             kwargs["queryset"] = Categoria.objects.filter(baja=False)
#         return super().formfield_for_foreignkey(db_field, request, **kwargs)

# #permite mostrar y editar modelos relacionados en línea dentro de la interfaz de administración de otro modelo     
# class InscripcionInline(admin.TabularInline):
#     model = Inscripcion

# #agregar la funcionalidad de creación de instancias de Inscripcion
# class ComisionAdmin(admin.ModelAdmin):
#     inlines = [
#         InscripcionInline,
#     ]

#permite mostrar y editar modelos relacionados en línea dentro de la interfaz de administración de otro modelo     
class DetalleInline(admin.TabularInline):
    model = Det_Compras

#agregar la funcionalidad de creación de instancias de Inscripcion
class ComprasAdmin(admin.ModelAdmin):
    inlines = [
        DetalleInline,
    ]


#registros de modelos en Admin personalizado
sitio_admin = ComprasSite(name='comprassite')
sitio_admin.register(Persona,PersonaAdmin)
sitio_admin.register(Clasificacion,ClasificacionAdmin)
sitio_admin.register(Producto,ProductoAdmin)
sitio_admin.register(Cab_Compras, ComprasAdmin)
# sitio_admin.register(Curso,CursoAdmin)
# sitio_admin.register(Comision,ComisionAdmin)
# sitio_admin.register(Usuario,UserAdmin)
# sitio_admin.register(Group, GroupAdmin)
# admin.site.register(Curso,CursoAdmin)


