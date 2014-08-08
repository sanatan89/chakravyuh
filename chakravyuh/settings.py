"""
Django settings for chakravyuh project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from logging.handlers import SysLogHandler
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 's)!fm^=6o6&$ft+4_@v3aoma37e9qfz)6cf-beeyzm4ci5b4^7'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

TEMPLATE_DIRS = os.path.join(os.path.dirname(os.path.dirname(__file__)),'templates')

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

ALLOWED_HOSTS = []

MEDIA_ROOT = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'media')
MEDIA_URL = '/media/'
# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'accounts',
    'puzzles'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'chakravyuh.urls'

WSGI_APPLICATION = 'chakravyuh.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/
STATIC_ROOT = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'static')
STATIC_URL = '/static/'

import logging
LOG_FILE_PATH = os.path.join('/tmp', 'logs')
LOG_FILE = LOG_FILE_PATH + '/chakravyuh.log'
LOG_FORMAT = "%(filename)s:%(lineno)d || %(name)s || %(message)s"
DATE_FORMAT = "%Y-%m-%d %H:%M:%S"
root_logger = logging.getLogger()
root_logger.setLevel(logging.DEBUG)
handler = SysLogHandler(facility=16)
handler.setFormatter(logging.Formatter(LOG_FORMAT, DATE_FORMAT))
root_logger.addHandler(handler)


LOGIN_URL = '/accounts/login/'
LOGOUT_URL = '/accounts/logout/'
