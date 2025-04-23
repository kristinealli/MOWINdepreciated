"""
This module contains the settings for the Django flashcards application.
It includes configurations for secret management, database connections,
static files, and installed applications.
"""

from pathlib import Path
import io
import os
from urllib.parse import urlparse
import environ
import google.auth
from google.cloud import secretmanager as sm

# Pull django-environ settings file, stored in Secret Manager
SETTINGS_NAME = "application_settings"

_, project = google.auth.default()
client = sm.SecretManagerServiceClient()
name = f"projects/{project}/secrets/{SETTINGS_NAME}/versions/latest"
payload = client.access_secret_version(name=name).payload.data.decode("UTF-8")

env = environ.Env()
env.read_env(io.StringIO(payload))

# Load Django secret key value via django-environ
# SECURITY WARNING: keep the Django secret key used in production secret!
SECRET_KEY = env("SECRET_KEY")

# Load DEBUG value via django-environ
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env("DEBUG", default=False)


CLOUDRUN_SERVICE_URL = 'https://mowin-264520351136.us-central1.run.app'

if CLOUDRUN_SERVICE_URL:
    parsed_url = urlparse(CLOUDRUN_SERVICE_URL)
    ALLOWED_HOSTS = [parsed_url.netloc]
else:
    raise ValueError("CLOUDRUN_SERVICE_URL must be defined in production!")

CSRF_TRUSTED_ORIGINS = [
    'https://mowin-264520351136.us-central1.run.app',
]

# Load DATABASES value via django-environ
DATABASES = {"default": env.db()}

# Base Directory
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Initialize environment variables
env = environ.Env()
environ.Env.read_env()

# Static Files
STATIC_URL = f'https://storage.googleapis.com/{env("GS_BUCKET_NAME")}/static/'  # Serve static files from GCS
STATICFILES_DIRS = [
    BASE_DIR / 'cards/static',  # Local static files for development
]
DEFAULT_FILE_STORAGE = "storages.backends.gcloud.GoogleCloudStorage"
STATICFILES_STORAGE = "storages.backends.gcloud.GoogleCloudStorage"

# GCS Settings
GS_BUCKET_NAME = env("GS_BUCKET_NAME")  # Ensure this is set in your environment variables
GS_DEFAULT_ACL = "publicRead"  # Allows public access to static files


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'cards',
    'flashcards',  # Include for custom data migration in Google Cloud workshop
    "storages",    # Include for Google Cloud Storage Bucket
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware', 
    'django.contrib.sessions.middleware.SessionMiddleware',  # Required for admin
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',  # Required for admin
    'django.contrib.messages.middleware.MessageMiddleware',  # Required for admin
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'flashcards.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'flashcards.wsgi.application'


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


SECRET_KEY = os.getenv("SECRET_KEY", "5FVo0DSVHCL4J1wTqqQpu7YrcpiGZkkdP81xmEbyHxCRFhKeNv")
DEBUG = os.getenv("DEBUG", "True") == "True"

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'flashcards_db',
        'USER': 'pguser',
        'PASSWORD': 'plAgue2020',
        'HOST': '/cloudsql/mowin-learning-app:us-central1:mowin-postgres',
        'PORT': '',
    }
}

# Redirect to the dashboard after login
LOGIN_REDIRECT_URL = '/dashboard/'

# Optional: Redirect to home after logout
LOGOUT_REDIRECT_URL = '/'
