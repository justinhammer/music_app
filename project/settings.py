"""
Django settings for project project.

Generated by 'django-admin startproject' using Django 1.8.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

FMAKEY = 'PDCK2LQJIAKLRZFL'
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'smqe=1n9+^ip)+ap**3c48n&x%mq^m7eb^$5a8(kwcw@2szks^'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

AUTH_USER_MODEL = 'main.CustomUser'
SOCIAL_AUTH_USER_MODEL = 'main.CustomUser'

SOCIAL_AUTH_LOGIN_REDIRECT_URL = 'http://127.0.0.1:8000/' 
SOCIAL_AUTH_LOGIN_URL = 'http://127.0.0.1:8000/login'

SOCIAL_AUTH_TWITTER_KEY = 'UycxGj8SpTIY8nIisz7LmSzUS' 
SOCIAL_AUTH_TWITTER_SECRET = '4AIhpNkc9N3g2eVTSc7paZfTv6ypz8GJkV8V0MXmZ0eAZlm52X'

SOCIAL_AUTH_FACEBOOK_KEY = '703309349803596'
SOCIAL_AUTH_FACEBOOK_SECRET = '941183a69855ff49e1228480b88fbad5'

SOCIAL_AUTH_INSTAGRAM_KEY = 'a79f8c3c553c4c3082250cee418bf975'
SOCIAL_AUTH_INSTAGRAM_SECRET = '55acdbf65ce041aaabf8d80361c8ea04'

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'main',
    'social.apps.django_app.default',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

AUTHENTICATION_BACKENDS = (  
    'social.backends.facebook.FacebookOAuth2',
    'social.backends.google.GoogleOAuth2',
    'social.backends.twitter.TwitterOAuth',
    'social.backends.instagram.InstagramOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)

ROOT_URLCONF = 'project.urls'

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
                'social.apps.django_app.context_processors.backends',
                'social.apps.django_app.context_processors.login_redirect',
            ],
        },
    },
]

WSGI_APPLICATION = 'project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'music_app',
        'HOST': '127.0.0.1',
        'USER': 'root',
        'PASSWORD': 'BYUCougars4321',
        'PORT': '',
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
