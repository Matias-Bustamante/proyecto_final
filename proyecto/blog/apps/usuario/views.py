from django.shortcuts import render,redirect
from .models import Usuario
from .forms import UsuarioForm, CreacionUsuario
from django.contrib.auth import authenticate, login
# Create your views here.

def registro(request): 
    contexto={ 
        'user':''
    }
    if request.method=="POST": 
        nombre=request.POST["nombre"]
        apellido=request.POST["apellido"]
        password=request.POST["password"]

        if (nombre and apellido and password): 
           
            usuario=Usuario.objects.filter(nombre=nombre)
            usuario_ap=Usuario.objects.filter(apellido=apellido)
            
            if (usuario and usuario_ap): 
                usuario=Usuario.objects.filter(nombre=nombre)
                contexto={ 
                    "user":usuario,
                    'apellido':usuario_ap
                }
               
                return render(request,'registration/login.html',contexto)
            else: 
                 usuario=Usuario(nombre=nombre,apellido=apellido,contrasenia=password)
                 usuario.save()
                 return redirect(to="sesion") 
                
       

  
    return render(request,"registration/login.html",contexto)


def sesion(request): 
    
    if (request.method=="POST"): 
        usuario=request.POST["usuario"]
        password=request.POST["password"]
        
        if (usuario and password): 
            usuario=Usuario.objects.filter(nombre__icontains=usuario)
            passw=Usuario.objects.filter(contrasenia__icontains=password)
           
            if (usuario and passw): 
                return redirect(to='blog:comentario')
            else: 
                contexto={ 'param':usuario}
                return render(request,'sesion.html',contexto)  
               
            
    return render(request,'sesion.html')




