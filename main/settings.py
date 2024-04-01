from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-_y+sp^6$s$!elm+vaurp3wdtkiy0j$va64m0tc4!-zfgbqten$'

DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',

    #third party
    'allauth',
    'allauth.account',
    'allauth.socialaccount',

    #social providers
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.github',
    'allauth.socialaccount.providers.facebook',

    'crispy_forms',
    'crispy_bootstrap5',
    'ckeditor',

    #local
    'core.apps.CoreConfig',
    'instructor.apps.InstructorConfig',
    'student.apps.StudentConfig',
    'course.apps.CourseConfig',
    'user.apps.UserConfig',
    'payments.apps.PaymentsConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',
]

ROOT_URLCONF = 'main.urls'

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"
SITE_ID = 1

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates/')],
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

WSGI_APPLICATION = 'main.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

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

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Africa/Nairobi'
USE_I18N = True

USE_TZ = True

STRIPE_PUBLISHABLE_KEY = 'pk_test_51MNsCZA7TkEZUV8Fn7IYOIiYzUmLYE1kYXwA3Xdhp2rRqnaZH5el7dIU5vqs5JWfFFyCt2okLF5B6VbZoDWJnzNv00kIK41Z8p'
STRIPE_SECRET_KEY = 'sk_test_51MNsCZA7TkEZUV8FHT5uNExuATedXUAC6Q2jHNk6XQpl374cezqx4ss6UEXuzxP9NDRJamO7pRkNBkk6i8HK96PR00gE7AL1vW'

STATIC_URL = 'static/'
# STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static/')
]
CKEDITOR_BASEPATH = "/static/ckeditor/ckeditor/"
CKEDITOR_UPLOAD_PATH = "media/uploads/"

MEDIA_URL = 'media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

ACCOUNT_AUTHENTICATED_LOGIN_REDIRECTS = True
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_AUTHENTICATION_METHOD = "username_email"
ACCOUNT_CONFIRM_EMAIL_ON_GET = False
ACCOUNT_EMAIL_CONFIRMATION_ANONYMOUS_REDIRECT_URL = '/'
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 1
ACCOUNT_EMAIL_VERIFICATION = "none"
ACCOUNT_EMAIL_MAX_LENGTH = 200
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_CHANGE_EMAIL = True
ACCOUNT_SIGNUP_REDIRECT_URL = 'users:update_profile'
ACCOUNT_LOGIN_ATTEMPTS_LIMIT = 5
ACCOUNT_RATE_LIMITS = {
    "change_password": "5/m",
    "manage_email": "10/m",
    "reset_password": "20/m",
    "reset_password_email": "5/m",
    "reset_password_from_key": "20/m",
    "signup": "20/m",
}
ACCOUNT_LOGIN_ATTEMPTS_TIMEOUT = 1200
ACCOUNT_EMAIL_CONFIRMATION_COOLDOWN = 540
ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = True
ACCOUNT_LOGOUT_ON_PASSWORD_CHANGE = True
ACCOUNT_PRESERVE_USERNAME_CASING = False
ACCOUNT_LOGIN_ON_PASSWORD_RESET = True
ACCOUNT_SESSION_REMEMBER = True
ACCOUNT_USERNAME_BLACKLIST = ['admin', 'test', 'user', 'root', 'superuser', 'moderator', 'guest', 'support', 'service', '1234', '12345', 'banned', 'hacker', 'staff', 'owner', '123456', '12345678']
ACCOUNT_USER_MODEL_EMAIL_FIELD = "email"
ACCOUNT_USER_MODEL_USERNAME_FIELD = "username"
ACCOUNT_USERNAME_MIN_LENGTH = 4
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE = True
LOGIN_REDIRECT_URL = '/'
ACCOUNT_EMAIL_SUBJECT_PREFIX = 'EduConnect - '

SOCIALACCOUNT_EMAIL_AUTHENTICATION_AUTO_CONNECT = True
CSRF_TRUSTED_ORIGINS = [
    'https://educonnect.com/',
    'https://www.educonnect.com/',
]

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'educonnect.vstech.co.ke'
EMAIL_PORT = 465
EMAIL_HOST_USER = 'learning@educonnect.vstech.co.ke'
EMAIL_HOST_PASSWORD = 'OCE^?I5}1}H1'
EMAIL_USE_SSL = True
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER