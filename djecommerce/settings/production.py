from .base import *
from decouple import config

DEBUG = config('DEBUG')
ALLOWED_HOSTS = ['ip-address','0.0.0.0', 'hevitall.herokuapp.com']

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'}
]




DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'd3db6vmt3idg58',
        'USER': 'vuslunkabhcyvg',
        'PASSWORD': 'e8ddc08d8e208678c1b87e887d85e1caeb5843542ce96dbb8f35a1c71414743c',
        'HOST': 'ec2-54-208-96-16.compute-1.amazonaws.com',
        'PORT': '5432',
    }
}


STRIPE_PUBLIC_KEY = config('STRIPE_LIVE_PUBLIC_KEY')
STRIPE_SECRET_KEY = config('STRIPE_LIVE_SECRET_KEY')
