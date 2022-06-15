from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import UserEditForm,RegistroCustom

# Create your views here.


def inicio(request):
    return render(request, 'index.html')
def about(request):
    return render(request, 'about.html')

def registro(request):
    if request.method == 'POST':
        form = RegistroCustom(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'perfil.html', {'mensaje':f"Usuario creado correctamente"})
        else:
            form=RegistroCustom()
            return render(request, 'registro.html', {'mensaje':f"Datos Incorrectos","form":form})
    else:
        form = RegistroCustom()
        return render(request, 'registro.html', {'form': form})

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return render(request, 'index.html', {'mensaje':f"Bienvenido {username}"})
            else:
                form=AuthenticationForm()
                return render(request, 'login.html', {'mensaje':f"Datos Incorrectos","form":form})
        else:
            form=AuthenticationForm()
            return render(request, 'login.html', {'mensaje':f"Datos Incorrectos","form":form})
    else:
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})

def logout_request(request):
    
    logout(request)
    mensaje = "Has cerrado sesión"
    return render(request, 'index.html', {'mensaje':mensaje})

def perfil(request):
    return render(request, 'perfil.html')

#decorador que hace que solo pueda acceder a la vista si esta logueado
@login_required
def editar_perfil(request):

    username=request.user.username
    
    if request.method == 'POST':
        form = UserEditForm(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            request.user.email = info['email']
            psw = info['password1']
            request.user.set_password(psw)
            request.user.save()

            return render(request, 'perfil.html', {'mensaje':f"Usuario {username} modificado correctamente"})

    else:
        formulario = UserEditForm(initial={'email':request.user.email})
        
        return render(request, 'editar_perfil.html',{'formulario':formulario,'username':username})
    
    

