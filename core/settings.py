"""
Django settings for omega_champions project.

Generated by 'django-admin startproject' using Django 3.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import os
gettext = lambda s: s

DATA_DIR = os.path.dirname(os.path.dirname(__file__))
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/
from core.utils import dev_template_config, prod_template_config

# SECURITY WARNING: keep the secret key used in production secret!
with open(os.path.join(BASE_DIR, 'secret_key.txt')) as f:
    SECRET_KEY = f.read().strip()

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = (os.environ.get('DJANGO_DEBUG', 'True') == 'True')

ALLOWED_HOSTS = ['localhost','hamroloksewa.com','127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

INNER_APPS = [
    'apps.user',
    'apps.package',
]

THIRD_PARTY_APPS = [
    'rest_framework',
    'drf_spectacular',
    'rest_framework_simplejwt',
    'rest_framework_simplejwt.token_blacklist',
        'corsheaders',

]

INSTALLED_APPS += THIRD_PARTY_APPS
INSTALLED_APPS += INNER_APPS


MIDDLEWARE = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    # 'cms.middleware.utils.ApphookReloadMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'cms.middleware.user.CurrentUserMiddleware',
    # 'cms.middleware.page.CurrentPageMiddleware',
    # 'cms.middleware.toolbar.ToolbarMiddleware',
    # 'cms.middleware.language.LanguageCookieMiddleware',
]

FILE_UPLOAD_HANDLERS = [
    'django.core.files.uploadhandler.MemoryFileUploadHandler',
    'django.core.files.uploadhandler.TemporaryFileUploadHandler',
]

AUTHENTICATION_BACKENDS = [
    'apps.user.backend.PhoneNumberBackend',  # Use the correct path based on your directory structure
    'django.contrib.auth.backends.ModelBackend',
]


CORS_ALLOW_ALL_ORIGINS = True

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
    # 'DEFAULT_PERMISSION_CLASSES': [
    #     'rest_framework.permissions.IsAuthenticated',
    # ],
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}
SPECTACULAR_SETTINGS = {
    'TITLE': 'Hamro Loksewa API',
    'DESCRIPTION': '',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False,
    'COMPONENT_SPLIT_REQUEST': True
    # OTHER SETTINGS
}

ROOT_URLCONF = 'core.urls'

if not DEBUG:
    SECURE_BROWSER_XSS_FILTER = True

if (os.environ.get('DJANGO_DEBUG', 'True') == 'True'):
    TEMPLATES = [dev_template_config]
else:
    TEMPLATES = [prod_template_config]

# DATABASES = {
#     'default': {
#         'ENGINE': os.environ.get("SQL_ENGINE", "django.db.backends.postgresql"),
#         'HOST': os.environ.get("SQL_HOST", "localhost"),
#         'NAME': os.environ.get("SQL_PASSWORD", "postgres"),
#         'PASSWORD': os.environ.get("SQL_PASSWORD", "postgres"),
#         'PORT': os.environ.get("SQL_PORT", "5432"),
#         'USER': os.environ.get("SQL_USER", "postgres"),
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': os.environ.get("SQL_ENGINE", "django.db.backends.sqlite3"),
        'NAME': os.environ.get("SQL_NAME", os.path.join(BASE_DIR, "db.sqlite3")),
    }
}

WSGI_APPLICATION = 'core.wsgi.application'


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

# LANGUAGES = (
#     ## Customize this
#     ('en', gettext('en')),
#     ('ne', gettext('ne'))
# )
LANGUAGE_CODE = 'en'

TIME_ZONE = 'Asia/Kathmandu'

USE_I18N = False

USE_L10N = True

USE_TZ = True

# LOCALE_PATHS = [
#     os.path.join(BASE_DIR, 'locale')
# ]
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

X_FRAME_OPTIONS = 'SAMEORIGIN'

WEBPACK_LOADER = {
    'DEFAULT': {
        'STATS_FILE': os.path.join(BASE_DIR, 'static', 'webpack-stats.json'),
    },
}

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(DATA_DIR, 'media')

STATIC_URL = '/public/'
# use in deployment
STATIC_ROOT = os.path.join(BASE_DIR, 'core', 'static')

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_REDIRECT_URL = "/dashboard/"
LOGOUT_REDIRECT_URL = '/'