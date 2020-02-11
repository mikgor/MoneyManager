import os
from .local_settings import *
from django.utils.translation import ugettext_lazy as _

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = LS_SECRET_KEY

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = LS_ALLOWED_HOSTS


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'MoneyManagerApp'
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

ROOT_URLCONF = 'MoneyManager.urls'

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

WSGI_APPLICATION = 'MoneyManager.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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

AUTH_USER_MODEL = 'MoneyManagerApp.User'
LOGIN_REDIRECT_URL = 'DashboardView'
LOGOUT_REDIRECT_URL = 'LoginView'
LOGIN_URL= 'LoginView'

INCOME_CATEGORY_CHOICES = (
    ('IIL', _('Initial')), # Can't be moved; not sellectable
    ('ISY', _('Salary')),
    ('IPN', _('Pension')),
    ('IBS', _('Bonds')),
    ('IDS', _('Dividends')),
    ('IGF', _('Gift')),
    ('IGT', _('Grant')),
    ('IIT', _('Interest')),
    ('IOF', _('Offer')),
    ('IPE', _('Prize')),
    ('IRD', _('Refund')),
    ('IRL', _('Rental')),
    ('ISE', _('Sale')),
    ('ITR', _('Transfer')),
    ('IOR', _('Other')),
)

OUTCOME_CATEGORY_CHOICES = (
    ('OFD', _('Food')),
    ('OBS', _('Bills')),
    ('OTN', _('Tuition')),
    ('OHD', _('Household')),
    ('OAL', _('Apparel')),
    ('OCE', _('Culture')),
    ('OEN', _('Education')),
    ('OES', _('Electronics')),
    ('OEM', _('Entertainment')),
    ('OHH', _('Health')),
    ('IGF', _('Gift')),
    ('OIT', _('Installment')),
    ('OLN', _('Loan')),
    ('OHY', _('Hobby')),
    ('OTT', _('Transportation')),
    ('OTR', _('Transfer')),
    ('OOR', _('Other')),
)

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'
