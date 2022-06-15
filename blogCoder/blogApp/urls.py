from django.urls import path
from blogApp import views

urlpatterns = [
   
    path('', views.inicio, name="Inicio"), 
    path('login/', views.login_request, name="Login"),
    path('about/', views.about, name="About"),
    path('registro/', views.registro, name="Registro"),
    path('logout/', views.logout_request, name="Logout"),
    path('perfil/', views.perfil, name="Perfil"),
    path('editar-perfil/',views.editar_perfil,name="EditarPerfil"),
    path('crear_post/',views.crear_post,name="CrearPost"),
    path('posts/',views.posts,name="Posts"),
    path('eliminar_post/<int:id>',views.eliminar_post,name="EliminarPost"),
    path('post/<int:id>',views.post_individual,name="PostIndividual")
    
   
   
]
