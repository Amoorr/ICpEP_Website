"""
Django settings for ICpEP_Web project.

Generated by 'django-admin startproject' using Django 5.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-%v09o5+yqwi!58aa+@)tldy4b6aj_df5qrajd*4-d$-7qqjp&#'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'accounts',
    'marketplace',
    'event_calendar',
    'news',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'ICpEP_Web.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # This points to the templates folder in the root of your project
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


WSGI_APPLICATION = 'ICpEP_Web.wsgi.application'


# Using the unified database in the MySQL
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # Use MySQL backend
        'NAME': 'icpep_website',  # Database name
        'USER': 'root',  # Your MySQL username
        'PASSWORD': '1234',  # Your MySQL password
        'HOST': 'localhost',  # Typically localhost or 127.0.0.1
        'PORT': '3306',  # Default MySQL port
    }
}



# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Manila'
USE_TZ = True





# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'

# This is where your CSS files will be found
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static/'),
]


# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Defining the custom user model located in app 'accounts'
AUTH_USER_MODEL = 'accounts.CustomUser'

# URL of the login page
LOGIN_URL = 'login'

# URL of redirection when the users want to access the login page
LOGIN_REDIRECT_URL = 'student_dashboard'  # Redirect to student dashboard after login

# URL of redirection upon logging out
LOGOUT_REDIRECT_URL = 'login'

# Path to the directory where uploaded files will be stored
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# URL that serves the uploaded media files
MEDIA_URL = '/media/'



