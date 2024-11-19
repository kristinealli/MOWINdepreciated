LOGIN_REDIRECT_URL = 'dashboard'
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'unique-snowflake',
    }
}

import dj_database_url
import os

# Update the database configuration to use Heroku's DATABASE_URL
DATABASES = {
    'default': dj_database_url.config(default=os.environ.get('DATABASE_URL'))
}

# Configure static files for Heroku
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

# Simplify static file serving
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Ensure the app is secure
DEBUG = False
ALLOWED_HOSTS = ['mowin.herokuapp.com']