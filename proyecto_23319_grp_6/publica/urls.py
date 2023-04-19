from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home' ),
    path('home/<int:idUser>/', views.homeLogIn, name='homeUser' ),
    path('', views.home, name='home' ),
    path('login/', views.login, name='login' ),
    path('detailProduct/', views.detailProduct, name='detailProduct' ),
    path('formLogin/', views.formLogin, name='formLogin' )
     
]
