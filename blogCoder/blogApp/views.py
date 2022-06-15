from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required
from .forms import UserEditForm,RegistroCustom,PostForm
from .models import Post,Tag

# Create your views here.

def crear_post(request):
    nuevo_post=PostForm()
    tag1 = Tag.objects.crear_tag("Terror")
    tag2 = Tag.objects.crear_tag("Suspenso")
    tag3 = Tag.objects.crear_tag("Comedia")
    tag4 = Tag.objects.crear_tag("Drama")
    tag5 = Tag.objects.crear_tag("Accion")
    if request.method == 'POST':
        nuevo_post=PostForm(request.POST)
        if nuevo_post.is_valid():
            nuevo_post.save()   
            return render(request, 'posts.html', {'mensaje':f"Post creado correctamente"})
        else:
            return render(request, 'crear_post.html', {'mensaje':f"Datos Incorrectos",'nuevo_post':nuevo_post})
    
    
    return render(request, 'crear_post.html', {'nuevo_post':nuevo_post})
def posts(request):
    posts = Post.objects.all().order_by('-creado')
    return render(request, 'posts.html', {'posts':posts})

def post_individual(request,id):
    post=Post.objects.get(id=id)
    print(post.tags.all())
    return render(request,'post.html',{'post':post})

def eliminar_post(request,id):
    post = Post.objects.get(id=id)
    post.delete()
    return render(request, 'eliminar_post.html', {'mensaje':f"Post eliminado correctamente"})
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
                posts = Post.objects.all()
                return render(request, 'posts.html', {'mensaje':f"Bienvenido {username}",'posts':posts})
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
    
    

