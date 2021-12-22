
from .base import *

DEBUG = False 

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'UTN', 
        'USER':'postgres', 
        'PASSWORD':'root', 
        'HOST':'localhost', 
        'PORT':'',
    },
}
