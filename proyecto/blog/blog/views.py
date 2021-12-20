from django.shortcuts import render,redirect
from apps.usuario.models import Usuario

def index(request): 
    return render(request,"index.html")

def sesion(request): 

    if (request.method=="POST"): 
        nombre=request.POST["usuario"]
        contrasenia=request.POST["password"]

        if (nombre and contrasenia): 
            usuario=Usuario.objects.filter(nombre=nombre)
            passw=Usuario.objects.filter(contrasenia=contrasenia)

            if (usuario and passw): 
                return redirect(to="blog:comentario")


    return render(request,"sesion.html")