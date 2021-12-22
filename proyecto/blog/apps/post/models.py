from django.db import models
from apps.usuario.models import Usuario

# Create your models here.

class Categoria(models.Model): 
    id=models.AutoField(primary_key=True)
    nombre=models.CharField("Nombre de la Categoria" , max_length=150)
    descripcion=models.CharField('Descripción de la Categoria' ,max_length=150)
    estado=models.BooleanField('Activado/Desactivado', default=True)
    
    



    class Meta(): 
        verbose_name="Categoria"
        verbose_name_plural="Categorias"
    
    def __str__(self): 
        return self.nombre

  


class Post(models.Model): 
    id=models.AutoField(primary_key=True); 
    titulo=models.CharField('Titulo del Post', max_length=150, null=False, blank=False)
    descripcion=models.CharField('Descripción', max_length=110, null=False, blank=False)
    categoria=models.ForeignKey(Categoria,on_delete=models.CASCADE,null=False,blank=False)
    estado=models.BooleanField('Publicado/No Publicado', default=True)
    imagen=models.ImageField('Imagenes', blank=False,null=False, upload_to='post')
    contenido=models.TextField()
    fecha_creacion=models.DateField('Fecha de Creación', auto_now=False, auto_now_add=True)
    user=models.ForeignKey(Usuario, on_delete=models.CASCADE)


    class Meta(): 
        verbose_name="Post", 
        verbose_name_plural="Posts",
    
    def __str__(self): 
        return self.titulo


class Comentario(models.Model): 
    id=models.AutoField(primary_key=True); 
    mensaje=models.TextField()
    asunto=models.CharField(max_length=100,blank=False,null=False)
    fecha_alta=models.DateField(auto_now_add=True, auto_now=False); 
    user=models.ForeignKey(Usuario, on_delete=models.CASCADE)
   
    class Meta(): 
        verbose_name="Comentario", 
        verbose_name_plural="Comentarios"

    def __str__(self): 
        return str(self.user)

