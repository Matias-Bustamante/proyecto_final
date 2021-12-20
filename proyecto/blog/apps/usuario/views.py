from django.shortcuts import render,redirect
from .models import Usuario
from .forms import UsuarioForm, CreacionUsuario
from django.contrib.auth import authenticate, login
# Create your views here.

def registro(request): 
    
    if request.method=="POST": 
        nombre=request.POST["nombre"]
        apellido=request.POST["apellido"]
        password=request.POST["apellido"]

        if (nombre and apellido and password): 
            usuario=Usuario(nombre=nombre,apellido=apellido,contrasenia=password)
            usuario.save()
            return redirect(to="sesion")     
       

            
    return render(request,"registration/login.html")


def sesion(request): 
    
    if (request.method=="POST"): 
        usuario=request.POST["usuario"]
        password=request.POST["password"]

        if (usuario and password): 
            usuario=Usuario.objects.filter(nombre=usuario, contrasenia=password)

            if (usuario): 
                return redirect(to='blog:comentario')
            
    return render(request,'sesion.html')




