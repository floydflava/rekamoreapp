from .base import *
import dj_database_url


DEBUG = False
ALLOWED_HOSTS = ['0.0.0.0','127.0.0.1','hevitall.herokuapp.com']



# import dj_database_url

# ON_HEROKU = os.environ.get('ON_HEROKU')
# HEROKU_SERVER = os.environ.get('HEROKU_SERVER')

# if ON_HEROKU:
#     DATABASE_URL = 'postgres://vuslunkabhcyvg:e8ddc08d8e208678c1b87e887d85e1caeb5843542ce96dbb8f35a1c71414743c@ec2-54-208-96-16.compute-1.amazonaws.com:5432/d3db6vmt3idg58'
# else:
#    DATABASE_URL = 'sqlite:///' + os.path.join(BASE_DIR, 'db.sqlite3')


# 

# SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'}
]


# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'floyddipela',
#         'USER': 'floyddipela',
#         'PASSWORD': '',
#         'HOST': 'localhost',
#         'POST': '5432',
#     }
# }
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'heroku_9c9d4095a655b98',
#         'USER': 'b93b0ad0a2825c',
#         'PASSWORD': '98a7f30e',
#         'HOST': 'us-cdbr-east-04.cleardb.com',
#         'POST': '3306',
#     }
# }

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }
# db_from_env = dj_database_url.config(conn_max_age=600, ssl_require=True)
# DATABASES['default'].update(db_from_env)

STRIPE_PUBLIC_KEY = config('STRIPE_TEST_PUBLIC_KEY')
STRIPE_SECRET_KEY = config('STRIPE_TEST_SECRET_KEY')
