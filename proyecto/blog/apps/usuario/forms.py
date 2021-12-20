from django import forms
from .models import Usuario
from django.contrib.auth.forms import UserCreationForm

class UsuarioForm(forms.ModelForm): 
    
    class Meta: 
        model=Usuario
        fields='__all__'


class CreacionUsuario(UserCreationForm): 
    pass

    