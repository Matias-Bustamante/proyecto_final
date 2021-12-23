
from .base import *

DEBUG = True

ALLOWED_HOSTS = ['bloggrupo4.herokuapp.com']

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'ddnonj4ag9k45r', 
        'USER':'hgskhmyqgdczzg', 
        'PASSWORD':'5f9c777ac44e263ea4e665b4ae711dee0772ac9f2c14adea4fc9cadb8c2a725c', 
        'HOST':'ec2-52-54-167-8.compute-1.amazonaws.com', 
        'PORT':5432,
    },
}

STATICFILES_DIRS=(os.path.join(os.path.dirname(BASE_DIR)),'static')


MEDIA_URL='/media/'
MEDIA_ROOT=os.path.join(os.path.dirname(BASE_DIR),'media/')
