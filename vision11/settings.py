from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-_%m7ea3s-j7c!%#$1kcr5rd9l%v0+3r2)kfokng)=fl!i992(h'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'mainAPP',
    'usermanagerAPP',
    'rest_framework',
    'channels',
    'chatsupportAPP',
    'whitenoise.runserver_nostatic',
    'payments'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'vision11.urls'


TEMPLATES_DIRS = [
    os.path.join(BASE_DIR, 'templates')
]


if DEBUG:
    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, 'statics')
    ]
else:
    STATIC_ROOT = os.path.join(BASE_DIR, 'statics')


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': TEMPLATES_DIRS,
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

WSGI_APPLICATION = 'vision11.wsgi.application'
  


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'd801e0m4sdtpdu',
#         'HOST': 'ec2-3-231-254-204.compute-1.amazonaws.com',
#         'PORT': 5432,
#         'USER': 'jbyoptjqibgoyy',
#         'PASSWORD': 'aeb05c686bab5d837a7817563ffb3145533248701debdd176438901ab9313d0b'
#     }
# }


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


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


STATIC_URL = 'static/'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join('BASE_DIR', 'statics/imgs')
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]


# social auth settings (django-allauth)
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '348112354410-olp3k7jc99r6ld908v2qgt0hf7iqkfqm.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = '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'


SITE_ID = 1
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'
ACCOUNT_FORMS = {
    'signup': 'usermanagerAPP.forms.Signup_details',
}


# Provider specific settings
SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'APP': {
            'client_id': SOCIAL_AUTH_GOOGLE_OAUTH2_KEY,
            'secret': SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET,
            'key': ''
        }
    }
}


# email configuration
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_HOST_USER = "no.reply.python.py@gmail.com"
EMAIL_HOST_PASSWORD = "qwerty@123"
EMAIL_USE_TLS = True


# auth user model
AUTH_USER_MODEL = "usermanagerAPP.User1"


# django all-auth settings
ACCOUNT_AUTHENTICATION_METHOD = "username_email"
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 1
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = "mandatory"
ACCOUNT_LOGIN_ATTEMPTS_LIMIT = 5
ACCOUNT_LOGIN_ATTEMPTS_TIMEOUT = 3600  # 1 hrs block
ACCOUNT_LOGOUT_ON_PASSWORD_CHANGE = True
SOCIALACCOUNT_LOGIN_ON_GET = True

# ASGI APP
ASGI_APPLICATION = 'vision11.asgi.application'


# RAZOR PAY DUMMY CREDENTIALS
RAZOR_KEY_ID = "rzp_test_48HADa6gNmd6ks"
RAZOR_KEY_SECRET = "cs3QfR8Wb6WQ7ZidL5Fr5P29"


# Channel Layer Setup
CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": [("127.0.0.1", 6379)],
        },
    },
}
