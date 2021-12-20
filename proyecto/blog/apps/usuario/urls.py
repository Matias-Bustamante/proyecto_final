from django.urls import path
from .views import registro, sesion

urlpatterns=[ 
    path('registro/', registro,name="registro"), 
    path('sesion/', sesion,name="sesion"),
   
]
