from django.urls import path
from blogApp import views

urlpatterns = [
   
    path('', views.inicio, name="Inicio"), 
    path('login/', views.login_request, name="Login"),
    path('about/', views.about, name="About"),
    path('registro/', views.registro, name="Registro"),
    path('logout/', views.logout_request, name="Logout"),
    path('perfil/', views.perfil, name="Perfil"),
    path('editar-perfil/',views.editar_perfil,name="EditarPerfil")
    
   
   
]
