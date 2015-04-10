# flake8: noqa

import os
from sys import path


BASE_DIR = os.path.dirname(os.path.dirname(__file__))
SITE_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SITE_NAME = os.path.basename(BASE_DIR)

# Add our project to our pythonpath, this way we don't need to type our project
# name in our dotted import paths:
path.append(BASE_DIR)


DEBUG = False
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Ann Onymous', 'change.me@gmail.com'),
)

TIME_ZONE = 'Europe/London'
LANGUAGE_CODE = 'en-gb'

SITE_ID = 1

USE_I18N = True
USE_L10N = True
USE_TZ = True

MEDIA_ROOT = os.path.join(SITE_ROOT, 'media')
MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(SITE_ROOT, 'assets')
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)


# Note: This key should only be used for development and testing.
SECRET_KEY = r"ur97rr4qrrv&fz7egjn7vx#ohgb-r6thho%qn#v#t!@fez507u"


TEMPLATE_DIRS = (
    os.path.join(SITE_ROOT, "templates"),
)

MIDDLEWARE_CLASSES = (
    # Default Django middleware.
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

# We're using bcrypt: https://docs.djangoproject.com/en/dev/topics/auth/passwords/#using-bcrypt-with-django
PASSWORD_HASHERS = (
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
    'django.contrib.auth.hashers.BCryptPasswordHasher',
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.SHA1PasswordHasher',
    'django.contrib.auth.hashers.MD5PasswordHasher',
    'django.contrib.auth.hashers.CryptPasswordHasher',
)

ROOT_URLCONF = '{{ project_name }}.urls'


INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django.contrib.humanize',

    'django.contrib.admin',

    'djcelery',

    '{{ project_name }}.apps.users',
)

AUTH_USER_MODEL = 'users.User'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

WSGI_APPLICATION = '{{ project_name }}.wsgi.application'

# Celery
BROKER_URL = 'amqp://guest:guest@localhost:5672//'
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
