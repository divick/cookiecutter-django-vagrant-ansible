"""
Django settings for {{cookiecutter.project_slug}} project.
"""

import os

APP_NAME = "{{cookiecutter.project_slug}}"
DEBUG = True

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'nmxm7ys_vpaqtl5v!v4v!47ae_21m6f(6ykasp@7+xy-ksz&qd'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition
INSTALLED_APPS = [
    {% for app in cookiecutter.ansible.my_apps %}
    {{app}},
    {% endfor %}
    {% for app in cookiecutter.ansible.installed_apps %}
    {{app}},
    {% endfor %}
]

NEWSLETTER_CONFIRM_EMAIL = False

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = "{{cookiecutter.project_slug}}.urls"

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, "templates"),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'imagestore.context_processors.imagestore_processor',
                # Needed to have settings defined in SETTINGS_EXPORT
                # available in settings
                'django_settings_export.settings_export',
            ],
        },
    },
]

# Settings to make available in templates
SETTINGS_EXPORT = [
    'SUPPORT_EMAIL',
    'CONTACTUS_EMAIL',
    'APP_NAME',
    'DOMAIN_NAME',
]

WSGI_APPLICATION = '%s.wsgi.application' % (APP_NAME)
SESSION_ENGINE = "django.contrib.sessions.backends.signed_cookies"

# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.'
                'UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.'
                'MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.'
                'CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.'
                'NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'
USE_I18N = True
USE_L10N = True
USE_TZ = True
SITE_ID = 1


STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    # other finders..
    'compressor.finders.CompressorFinder',
)

# Location of static files which are not tied to any app and
# collectstatic will also look for in the directories defined
# here apart from looking at static directory of each app defined
# in INSTALLED_APPS
STATICFILES_DIRS = [
    os.path.join("%s" % BASE_DIR, "static"),
]

# Url prefix where the static files will be looked for
STATIC_URL = '/static/'
# Url prefix where the media files will be looked for
MEDIA_URL = os.path.join(STATIC_URL, 'media/')


LOGIN_REDIRECT_URL = "/users/myprofile/"
LOGIN_URL = "/accounts/login/"


AUTH_USER_MODEL = 'users.User'

# django-allauth setting
ACCOUNT_LOGOUT_REDIRECT_URL = "/"
ACCOUNT_LOGIN_REDIRECT_URL = "/accounts/login/"
ACCOUNT_USER_MODEL_USERNAME_FIELD = None
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_ADAPTER = 'users.adapter.UserAccountAdapter'
# ACCOUNT_SIGNUP_FORM_CLASS = 'api.forms.UserSignupForm'
ACCOUNT_FORMS = {
    'signup': 'users.forms.UserSignupForm'
}
ACCOUNT_EMAIL_VERIFICATION = "mandatory"
# ACCOUNT_EMAIL_VERIFICATION="optional"
ACCOUNT_DEFAULT_HTTP_PROTOCOL = "http"

# django-guardian related setting
# ANONYMOUS_USER_ID = -1

SOCIALACCOUNT_ADAPTER = 'users.adapter.SocialAccountAdapter'
SOCIALACCOUNT_AUTO_SIGNUP = True
SOCIALACCOUNT_PROVIDERS = {
    'facebook': {
        'SCOPE': ['email', 'public_profile', ],
        'FIELDS': [
          'email', 'first_name', 'last_name', 'verified', 'gender',
          'location', 'picture',
         ],
        'AUTH_PARAMS': {'auth_type': 'reauthenticate'},
        'METHOD': 'oauth2',
        # 'METHOD': 'js_sdk',
        # 'LOCALE_FUNC': 'path.to.callable',
        'VERIFIED_EMAIL': False,
        'VERSION': 'v2.2'
    },
    'google': {
        'SCOPE': ['profile', 'email'],
        'AUTH_PARAMS': {'access_type': 'online'}
    }
}

AUTHENTICATION_BACKENDS = (
    # `allauth` specific authentication methods, such as login by e-mail
    "allauth.account.auth_backends.AuthenticationBackend",

    # Needed to login by username in Django admin, regardless of `allauth`
    "django.contrib.auth.backends.ModelBackend",
)

# Individual settings file override this
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

CELERY_RESULT_BACKEND = 'djcelery.backends.database:DatabaseBackend'
CELERYBEAT_SCHEDULER = 'djcelery.schedulers.DatabaseScheduler'
CELERY_SEND_TASK_ERROR_EMAILS = True
CELERY_IGNORE_RESULT = False
BROKER_URL = 'django://'


TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

MOMMY_CUSTOM_FIELDS_GEN = {
    'phonenumber_field.modelfields.PhoneNumberField': 'api.models.gen_phone'
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': 'localhost',
        'PORT': ''
    }
}

LOG_DIR = BASE_DIR
LOG_FILENAME = '%s.log' % (APP_NAME)
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '[%(asctime)s] %(levelname)s [%(module)s:%(funcName)s:'
                      '%(lineno)s %(process)d] %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(module)s:%(funcName)s:%(lineno)s::'
                      '%(message)s'
        },
    },
    'filters': {
    },
    'handlers': {
        'null': {
            'level': 'DEBUG',
            'class': 'logging.NullHandler',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'file': {
          'level': 'DEBUG',
          'class': 'logging.FileHandler',
          'formatter': 'verbose',
          'filename': os.path.join("%s" % (LOG_DIR), "%s" % (LOG_FILENAME))
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'filters': []
        }
    },
    'loggers': {
        '': {
            'handlers': ['mail_admins', 'file'],
            'level': 'DEBUG',
        },
        'django': {
            'handlers': ['mail_admins', 'file'],
            'propagate': True,
            'level': 'INFO',
        },
        'django.request': {
            'handlers': ['mail_admins', 'file'],
            'level': 'ERROR',
            'propagate': False,
        },
        'django.db.backends': {
            'handlers': ['console', 'mail_admins', 'file'],
            'level': 'ERROR',
            'propagate': False,
        },
        APP_NAME: {
            'handlers': ['mail_admins', 'file'],
            'level': 'DEBUG',
        },
        'auth': {
            'handlers': ['mail_admins', 'file'],
            'level': 'DEBUG',
        },
    }
}

IMAGESTORE_TEMPLATE="bases/base-member.html"
IMAGESTORE_SHOW_USER = True


COMPRESS_CSS_FILTERS = [
    'compressor.filters.css_default.CssAbsoluteFilter',
    'compressor.filters.cssmin.CSSMinFilter',
    'compressor.filters.cssmin.CSSCompressorFilter',
]

COMPRESS_OFFLINE=True

COMPRESS_PRECOMPILERS = (
    ('text/x-scss', 'sass --scss {infile} {outfile}'),
)

AWS_HEADERS = {
    # see http://developer.yahoo.com/performance/rules.html#expires
    'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
    'Cache-Control': 'max-age=94608000',
}
