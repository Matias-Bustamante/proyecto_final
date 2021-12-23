from django.shortcuts import render,redirect
from .models import Post,Categoria,Comentario
from apps.usuario.models import Usuario
from django.core import exceptions
from django.contrib.auth.views import LoginView

# Create your views here.

def index(request): 
    return render(request,"index.html")

def categoria(request): 
    return render(request,"categorias.html")

def post(request): 
    querysets=request.GET.get('buscar_post')
    coments=Comentario.objects.all()
    post=Post.objects.all()
    if (querysets): 
        categoria=Categoria.objects.filter(nombre__icontains=querysets)
        if (not categoria):  
            coments=Comentario.objects.filter(asunto=querysets).distinct('asunto')
            if (not coments): 
                 post=''
            else: 
                coments.order_by('-fecha_alta')[0:9]
                print(coments)
                

        else: 
            post=Post.objects.filter(categoria=Categoria.objects.get(nombre__icontains=querysets))  
    

       
    contexto={ 
        'posts':post, 
       'comentario':coments
    }
    return render(request,'post/post.html', contexto)


def filtrarFecha(request): 
    
    querysets=request.GET.get('buscar_fecha'); 
    post_fecha=Post.objects.all()
    comentario=Comentario.objects.all()
   
    if (not querysets): 
        print("la fecha esta vacia")
    else: 
        post_fecha=Post.objects.filter(fecha_creacion=querysets)
        comentario=Comentario.objects.filter(fecha_alta=querysets)
    contexto={ 
        'post': post_fecha,
        'fecha':comentario
    }
    return render(request,"buscarFecha.html", contexto)


def comments(request): 
    
    if (request.method=="GET"): 
        nombre=request.GET.get('nombre')
        apellido=request.GET.get('apellido')
        mensaje=request.GET.get('mensaje')
        asunto=request.GET.get('asunto')

        if (nombre and apellido and mensaje and asunto): 
            usuario_nombre=Usuario.objects.filter(nombre=nombre)
            usuario_apellido=Usuario.objects.filter(apellido=apellido)
            if (usuario_nombre and usuario_apellido): 
                pk=usuario_nombre[0] 
                comentario=Comentario(mensaje=mensaje,asunto=asunto, user=pk)
                comentario.save()
            else: 
                print("incorrecto")

            
               

    return render(request,"comentario/comentario.html")





