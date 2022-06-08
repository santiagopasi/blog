from django.urls import path
from blogApp import views

urlpatterns = [
   
    path('', views.inicio, name="Inicio"), 
    path('login/', views.login_request, name="Login"),
    path('contacto/', views.contacto, name="Contacto"),
    
   
   
]
