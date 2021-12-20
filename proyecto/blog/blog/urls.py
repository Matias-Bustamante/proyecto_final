"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include,re_path
from .views import sesion
from django.conf.urls.static import static
from django.conf import settings 
from django.views.static import serve 
from .views import index


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name="index"),
    path('sesion/',sesion,name="sesion"),
    path('blog/',include('apps.post.urls','blog')), 
    path('accounts/', include('django.contrib.auth.urls')),
    path('account/', include(('apps.usuario.urls','account'))),

    
]+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += [ 
        re_path(r'^media/(?P<path>.*)$', serve, { 
            'document_root':settings.MEDIA_ROOT,
        }),
    ]