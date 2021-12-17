from django.shortcuts import render
from .models import Post,Categoria
from django.core import exceptions

# Create your views here.

def index(request): 
    return render(request,"index.html")

def categoria(request): 
    return render(request,"categorias.html")

def post(request): 
    print(request.GET.get('buscar_post'))
    querysets=request.GET.get('buscar_post')
    post=Post.objects.all()
    if (querysets): 
        categoria=Categoria.objects.filter(nombre__icontains=querysets)
        if (not categoria): 
            post='' 
        else: 
            post=Post.objects.filter(categoria=Categoria.objects.get(nombre__icontains=querysets))           
        
       


    contexto={ 
        'posts':post
    }
    return render(request,'post/post.html', contexto)


def filtrarFecha(request): 
    
    querysets=request.GET.get('buscar_fecha'); 
    post_fecha=Post.objects.all()
   
    if (not querysets): 
        print("la fecha esta vacia")
    else: 
        post_fecha=Post.objects.filter(fecha_creacion=querysets)
    
    contexto={ 
        'post': post_fecha
    }
    return render(request,"buscarFecha.html", contexto)


def Comentario(request): 
    return render(request,"comentario/comentario.html")