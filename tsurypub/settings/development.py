from pathlib import Path
import dj_database_url
import environ
import os
from .base import *

DEBUG = env.bool('DEBUGG', default=False)
print("DEBUG IN DEVELOPTMENT: %s" % DEBUG)


SECRET_KEY = str(os.environ.get('SECRET_KEY'))

ALLOWED_HOSTS = ["*"] 


# Application definition


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASE = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': str(os.environ.get('DB_NAME')),
        'USER': str(os.environ.get('DB_USER')),
        'PASSWORD': str(os.environ.get('DB_PASSWORD')),
        'HOST':str(os.environ.get('DB_HOST')),
        'PORT':os.environ.get('DB_PORT'),
    }
}
