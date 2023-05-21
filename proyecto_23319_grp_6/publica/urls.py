from django.urls import path
from . import views


urlpatterns = [
   # path('home/', views.home, name='home' ),
    path('', views.detailProduct, name='detailProduct' ),
    path('login/', views.login_view, name='login' ),
    path('logout/', views.logout_view, name='logout' ),
    path('home/', views.detailProduct, name='detailProduct' ),
    #path('vender/', views.venderView, name='venderView' ),
    path('vender/', views.venderView, name='productos_index' ),
    path('formLogin/', views.formLogin, name='formLogin' ),
    path('home/<int:idUser>/', views.homeLogIn, name='homeUser' ),
    
    path('productos/', views.productos_index,name='productos_index'),
    path('productos/nuevo/', views.productos_nuevo,name='productos_nuevo'),
    path('productos/editar/<int:id>', views.productos_editar,name='productos_editar'),
    path('productos/eliminar/<int:id>', views.productos_eliminar,name='productos_eliminar'),

    path('clasificacionview/', views.ClasificacionListView.as_view(), name='clasificaciones_index_view'),
    path('clasificacion/viewnuevo', views.ClasificacionCreateView.as_view(), name='clasificaciones_nuevo_view'),
    path('clasificacion/vieweditar/<int:pk>', views.ClasificacionUpdateView.as_view(), name='clasificaciones_editar_view'),
    path('clasificacion/vieweliminar/<int:pk>', views.ClasificacionDeleteView.as_view(), name='clasificaciones_eliminar_view'),

]