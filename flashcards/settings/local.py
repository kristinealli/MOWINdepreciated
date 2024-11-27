import os

from pathlib import Path
from decouple import config



# Set BASE_DIR to the root of your project directory
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Secret Key
SECRET_KEY = config('SECRET_KEY', default='django-insecure-n@4_u_5mgxq^d52s05zv-^khjsn$mpl1576nd^9by7!ebgj$e5')

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
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME', 'flashcards'),
        'USER': os.getenv('DB_USER', 'kristinejohnson'),
        'PASSWORD': os.getenv('DB_PASSWORD', 'plAgue2020'),
        'HOST': os.getenv('DB_HOST', 'localhost'),  # or your Railway host
        'PORT': os.getenv('DB_PORT', '5432'),  # default PostgreSQL port
    }
}

# Configure static files for Heroku
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'cards/static'] 

# Simplify static file serving
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Ensure the app is secure
DEBUG = True
ALLOWED_HOSTS = ['localhost', '127.0.0.1']
ROOT_URLCONF = 'flashcards.urls'


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'cards',  
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware', 
    'django.contrib.sessions.middleware.SessionMiddleware',  # Required for admin
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',  # Required for admin
    'django.contrib.messages.middleware.MessageMiddleware',  # Required for admin
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['flashcards_app.cards.templates'],  # Add the path to the templates folder
        'APP_DIRS': True,     
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',  # Required for admin
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]