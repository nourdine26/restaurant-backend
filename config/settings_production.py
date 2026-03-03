import os
from .settings import *

DEBUG = False

# Autorisez Render et votre frontend
ALLOWED_HOSTS = ['.onrender.com', 'localhost', '127.0.0.1']

# Configuration STATIC_ROOT - TRÈS IMPORTANT
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

# Media files
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

# Base de données SQLite
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# CORS - mettez l'URL de votre Netlify
CORS_ALLOWED_ORIGINS = [
    'https://votre-site.netlify.app',
]
CORS_ALLOW_CREDENTIALS = True

# Sécurité pour Render
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True