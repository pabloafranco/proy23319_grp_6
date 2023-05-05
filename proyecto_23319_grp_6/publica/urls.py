from django.urls import path
from . import views

urlpatterns = [
   # path('home/', views.home, name='home' ),
    path('', views.detailProduct, name='detailProduct' ),
    path('login/', views.login, name='login' ),
    path('home/', views.detailProduct, name='detailProduct' ),
    path('vender/', views.venderView, name='venderView' ),
    path('formLogin/', views.formLogin, name='formLogin' ),
    path('home/<int:idUser>/', views.homeLogIn, name='homeUser' )
]