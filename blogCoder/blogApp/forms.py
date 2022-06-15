from .models import Post
from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

#creacion de posts
class PostForm(ModelForm):
   
    class Meta:
        model = Post
        fields = '__all__'



#me creo un custom registro para agregarle email
class RegistroCustom(UserCreationForm):

    email = forms.EmailField(label="email")

    class Meta:
        model=User
        fields=['email','username','password2']
        help_text={k:"" for k in fields}

class UserEditForm(UserCreationForm):
   
    email = forms.EmailField(label="email")
    password1=forms.CharField(label="Contraseña",widget=forms.PasswordInput)
    password2=forms.CharField(label="Repetir Contraseña",widget=forms.PasswordInput)

#definen permisos , asociar datos a alguna tabla se crea una class meta
    class Meta:
        model=User
        fields=['email','password1','password2']
        help_text={k:"" for k in fields}

