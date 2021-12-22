from .base import *

DEBUG = True

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



MEDIA_URL='/media/'
MEDIA_ROOT=os.path.join(os.path.dirname(BASE_DIR),'media/')

