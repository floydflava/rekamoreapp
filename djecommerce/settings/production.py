from .base import *
from decouple import config

DEBUG = config('DEBUG')
ALLOWED_HOSTS = ['ip-address', 'rekamoreapp.herokuapp.com']

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'}
]



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': config('dbmm61hsigstip'),
        'USER': config('mbtuwudtrrrcuv'),
        'PASSWORD': config('cabee50906b0678a588bb6361f47ffe403548893f30d3e119d47bafb2bc016ac'),
        'HOST': config('ec2-3-209-65-193.compute-1.amazonaws.com'),
        'PORT': '5432'
    }
}
DATABASES['default'] =  dj_database_url.config(default='postgres://mbtuwudtrrrcuv:cabee50906b0678a588bb6361f47ffe403548893f30d3e119d47bafb2bc016ac@ec2-3-209-65-193.compute-1.amazonaws.com:5432/dbmm61hsigstip')

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'dbmm61hsigstip',
#         'HOST': 'ec2-3-209-65-193.compute-1.amazonaws.com',
#         'PORT': 5432,
#         'USER': 'mbtuwudtrrrcuv',
#         'PASSWORD': 'cabee50906b0678a588bb6361f47ffe403548893f30d3e119d47bafb2bc016ac'
#     }
# }

django_heroku.settings(locals())
STRIPE_PUBLIC_KEY = config('STRIPE_LIVE_PUBLIC_KEY')
STRIPE_SECRET_KEY = config('STRIPE_LIVE_SECRET_KEY')
