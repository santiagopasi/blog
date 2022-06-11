from doctest import BLANKLINE_MARKER
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserEditForm(UserCreationForm):

    email = forms.EmailField(label="Modificar Email")
    password1=forms.CharField(label="Contraseña",widget=forms.PasswordInput)
    password2=forms.CharField(label="Repetir Contraseña",widget=forms.PasswordInput)

#definen permisos , asociar datos a alguna tabla se crea una class meta
    class Meta:
        model=User
        fields=['email','password1','password2']
        help_text={k:"" for k in fields}