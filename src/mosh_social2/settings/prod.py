from .base import *

# import sentry_sdk as sentry
# from sentry_sdk.integrations.django import DjangoIntegration

# DATABASES = {
#     'default': {
#         'ATOMIC_REQUESTS': True,
#         'CONN_MAX_AGE': config('CONN_MAX_AGE', default=60),
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': config('RDS_DB_NAME'),
#         'USER': config('RDS_USERNAME'),
#         'PASSWORD': config('RDS_PASSWORD'),
#         'HOST': config('RDS_HOSTNAME'),
#         'PORT': config('RDS_PORT'),
#         'TEST': {
#             'NAME': f'test_{config("RDS_DB_NAME")}',
#         },
#     }
# }

DATABASES = {
    'default': {
        'ATOMIC_REQUESTS': True,
        'CONN_MAX_AGE': config('CONN_MAX_AGE', default=60),
        'ENGINE': 'django.db.backends.mysql',
        'NAME': f'{config("PYTHONANYWHERE_USERNAME")}${config("PYTHONANYWHERE_DB_NAME")}',
        'USER': config('PYTHONANYWHERE_USERNAME'),
        'PASSWORD': config('PYTHONANYWHERE_PW'),
        'HOST': config('PYTHONANYWHERE_HOSTNAME'),
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        },
        'TEST': {
            'NAME': f'{config("PYTHONANYWHERE_USERNAME")}$test_{config("PYTHONANYWHERE_DB_NAME")}',
        },
    }
}

INSTALLED_APPS.append('storages')

STATICFILES_STORAGE = 'custom_storages.StaticStorage'
STATICFILES_LOCATION = 'static'

DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
MEDIAFILES_LOCATION = 'media'

AWS_ACCESS_KEY_ID = config('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = config('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = config('AWS_STORAGE_BUCKET_NAME')
AWS_S3_REGION_NAME = config('AWS_S3_REGION_NAME')
AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
AWS_DEFAULT_ACL = None
AWS_PRELOAD_METADATA = True
AWS_QUERYSTRING_AUTH = False

AWS_S3_OBJECT_PARAMETERS = {
    'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
    'CacheControl': 'max-age=94608000',
}

# sentry.init(config('SENTRY_DSN'), integrations=[DjangoIntegration()])
