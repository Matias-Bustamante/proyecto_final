from django.urls import path

from .views import index,categoria, post, filtrarFecha,comments

app_name='post'
urlpatterns = [
    path('index/',index, name="index"),
    path('categoria/',categoria, name="categoria"), 
    path('post/', post, name="post"),
    path("filtrarFecha/", filtrarFecha, name="filtrarFecha"), 
    path('comentario/', comments, name="comentario"), 
   
   
   
]
