import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: Enter your own SECRET_KEY here
SECRET_KEY = '+e@1*d2dt1h+x@vh59mukr0&&hp*yx7zdoif1h=4oz^b33b)s$'

ALLOWED_HOSTS = []
SITE_ID = 4

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.flatpages',
    'django_forms_bootstrap',
    'paypal.standard.ipn',
    'rest_framework',
    'tinymce',
    'emoticons',
    'disqus',
    'reusable_blog',
    'hello',  # called home in the examples even though earlier lesson advises to call hello
    'accounts',
    'paypal_store',
    'products',
    'magazines',
    'threads',
    'polls',
]

AUTH_USER_MODEL = 'accounts.User'
AUTHENTICATION_BACKENDS = ('django.contrib.auth.backends.ModelBackend', 'accounts.backends.EmailAuth',)
LOGIN_URL = '/login/'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
]

ROOT_URLCONF = 'we_are_social.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'we_are_social.wsgi.application'

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
USE_L10N = True
USE_TZ = True

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)

# required for pictures to show on blog
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

TINYMCE_JS_ROOT = os.path.join(BASE_DIR, "static", "js",
                               "tinymce", "tinymce.min.js")

# disqus
DISQUS_API_KEY = "9cVmxRfQIuL62vBaec8H5cG4UKnRSb3MNRqmfneDPQftZvj7rtqrWPOxmjfo8XBN"
DISQUS_WEBSITE_SHORTNAME = "codeinstitutesocialstaging"