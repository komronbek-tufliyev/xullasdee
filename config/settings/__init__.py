from .base import *
from .django_jazzmin import *

SECRET_KEY = env.str('SECRET_KEY')
ENVIRONMENT = env.str('ENVIRONMENT', default='development')
DEBUG = env.bool('DEBUG', default=True)
ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default=['*'])

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

if ENVIRONMENT == 'development':
    from .development import *
    # debug toolbar settings
    INTERNAL_IPS = [
        '127.0.0.1', 'localhost'
    ]
    INSTALLED_APPS += ['debug_toolbar']
    MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware']
    
elif ENVIRONMENT == 'production':
    from .production import *
else:
    raise ValueError('Invalid environment name')