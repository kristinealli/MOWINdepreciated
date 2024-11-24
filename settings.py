import dj_database_url
import os
from decouple import config
from flashcards.settings import BASE_DIR


LOGIN_REDIRECT_URL = 'dashboard'
CACHES = {
    'default': {
    'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    'LOCATION': 'unique-snowflake',
    }
}

# Load local configuration if it exists`` ``
try:
    pass
except ImportError:
    DATABASE_URL = config('DATABASE_URL')
    SECRET_KEY = config('SECRET_KEY')
    DEBUG = config('DEBUG', default=False, cast=bool)
    ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='localhost').split(',')

# Database configuration
DATABASES = {
    'default': dj_database_url.config(
        default=DATABASE_URL,
        conn_max_age=600,
        sslmode='disable'   # Add this line to disable SSL
    )
}

# Configure static files for Heroku
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

# Simplify static file serving
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Ensure the app is secure
DEBUG = False
ALLOWED_HOSTS = ['mowin.herokuapp.com']