from base import *
import dj_database_url

DEBUG = False

# load the ClearDB connection details from the environment variable
DATABASES = {
    'default': dj_database_url.config('CLEARDB_DATABASE_URL')
    }

# Stripe environment variables
STRIPE_PUBLISHABLE = os.getenv('STRIPE_PUBLISHABLE', 'pk_test_XM1d9ZdgN3EmNQrFAGaSbG9e')
STRIPE_SECRET = os.getenv('STRIPE_SECRET', 'sk_test_TT86LFyGyFQTGKlQ4kOEVrTc')

# Paypal environment variables
PAYPAL_NOTIFY_URL = 'http://9fa1441c.ngrok.io'
PAYPAL_RECEIVER_EMAIL = 'liam.cafearo@protonmail.com'

SITE_URL = 'https://code-inst-social-staging-liamc.herokuapp.com'
ALLOWED_HOSTS.append('code-inst-social-staging-liamc.herokuapp.com')

# Log DEBUG information to the console
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'DEBUG'),
        },
    },
}