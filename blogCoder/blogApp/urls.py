from django.urls import path
from blogApp import views

urlpatterns = [
   
    path('', views.inicio, name="Inicio"), 
    path('login/', views.login_request, name="Login"),
    path('contacto/', views.contacto, name="Contacto"),
    path('registro/', views.registro, name="Registro"),
    path('logout/', views.logout_request, name="Logout"),
    path('perfil/', views.perfil, name="Perfil"),
    path('editar-perfil/',views.editar_perfil,name="EditarPerfil")
    
   
   
]
