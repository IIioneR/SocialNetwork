from datetime import timedelta

from .base import *  # noqa: F403, F401

DEBUG = True

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

SIMPLE_JWT['ACCESS_TOKEN_LIFETIME'] = timedelta(minutes=30)


SWAGGER_SETTINGS = {
    'LOGIN_URL': '/admin/login/',
    'LOGOUT_URL': '/admin/logout/',
    'REFETCH_SCHEMA_WITH_AUTH': True,
    'PERSIST_AUTH': True,
    'SECURITY_DEFINITIONS': {'Bearer': {'type': 'apiKey', 'name': 'Authorization', 'in': 'header'}},
}

INSTALLED_APPS += ['drf_yasg']  # noqa F405
