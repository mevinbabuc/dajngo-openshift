"""
Django settings for themenu project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
DJ_PROJECT_DIR = os.path.dirname(__file__)
BASE_DIR = os.path.dirname(DJ_PROJECT_DIR)
DATA_DIR = os.environ.get('OPENSHIFT_DATA_DIR', '')
MEDIA_ROOT = os.path.join(DATA_DIR, 'media')

ON_OPENSHIFT = False
if 'OPENSHIFT_REPO_DIR' in os.environ:
    ON_OPENSHIFT = True


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/
SITE_ID = 1

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '!iudke*hi8vo#qyntq5yxm+p2itkuqg-m@bo8o%+cbnq(h%@@-'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Useful template tags:
    'django.contrib.humanize',

    # Admin panel and documentation:
    'django.contrib.admindocs',

    # GeoDjango
    'django.contrib.gis',

    # Custom apps
    'core'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'core.urls'

WSGI_APPLICATION = 'core.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases
if ON_OPENSHIFT:
    DATABASES = {
        'default': {
            'ENGINE': 'django.contrib.gis.db.backends.postgis',
            'NAME': 'themenu',
            'USER': 'adminzrsrnqm',
            'PASSWORD': 'K6DSmtuZLE8N',
            'HOST': '',
            'PORT': '',
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.contrib.gis.db.backends.postgis',
            'NAME': 'themenu',
            'USER': 'themenu',
            'PASSWORD': 'themenu',
            'HOST': 'localhost',
            'PORT': '',
        }
    }

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'static')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
if not ON_OPENSHIFT:
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

ADMINS = (
    ('Mevin Babu', 'mevinbabuc@gmail.com'),
)

SERVER_EMAIL = 'server@themenu.in'


# LOGGING CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#logging
# for more details on how to customize your logging configuration.
if ON_OPENSHIFT:
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'default': {
                'format': '[%(levelname)s][%(filename)s][%(funcName)s][%(asctime)s] %(message)s',
                'datefmt': '%Y-%m-%d %H:%M:%S %Z',
            },
        },
        'filters': {
            'require_debug_false': {
                '()': 'django.utils.log.RequireDebugFalse'
            }
        },
        'handlers': {
            'logtofile': {
                'level': 'DEBUG',
                'class': 'logging.handlers.RotatingFileHandler',
                'maxBytes': pow(1024, 3),  # 10 MB
                'backupCount': 3,
                'filename': os.path.join(DATA_DIR, '../logs', 'themenu.log'),
                'formatter': 'default',
            },
            'mail_admins': {
                'level': 'WARNING',
                'class': 'django.utils.log.AdminEmailHandler',
                # 'filters': ['require_debug_false',],
                'filters': [],
                'include_html': True,
            }
        },
        'loggers': {
            'themenu': {
                'level': 'DEBUG',
                'handlers': ['logtofile', 'mail_admins'],
            },
            'django': {
                'handlers': ['mail_admins'],
                'level': 'WARNING',
                'propagate': True,
            },
        }
    }

else:
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'handlers': {
            'file': {
                'level': 'DEBUG',
                'class': 'logging.FileHandler',
                'filename': '/home/vagrant/logs/django.log',
            },
        },
        'loggers': {
            'django.request': {
                'handlers': ['file'],
                'level': 'DEBUG',
                'propagate': True,
            },
        },
    }

ENV = "dev"
if ON_OPENSHIFT:
    ENV = "prod"
