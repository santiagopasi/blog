from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.models import User

# Create your views here.


def inicio(request):
    return render(request, 'index.html')
def contacto(request):
    return render(request, 'contacto.html')

def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Usuario creado correctamente")
        else:
            return HttpResponse("Datos incorrectos")
    else:
        form = UserCreationForm()
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
                return HttpResponse("Usuario o contraseña incorrectos")
        else:
            return HttpResponse("Datos incorrectos")
    else:
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})

def logout_request(request):
    
    logout(request)
    mensaje = "Has cerrado sesión"
    return render(request, 'index.html', {'mensaje':mensaje})

def perfil(request):
    return render(request, 'perfil.html')

