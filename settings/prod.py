from environs import Env
from pathlib import Path
import os

env = Env()
env.read_env()

DEBUG = False



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'bzp',
        'USER': 'gartman',
        'PASSWORD': 'Gartman95',
        'HOST': '127.0.0.1',
        'PORT': '5432'
    }
}
