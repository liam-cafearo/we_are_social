from base import *

DEBUG = True

INSTALLED_APPS.append('debug_toolbar')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Stripe environment variables
STRIPE_PUBLISHABLE = os.getenv(
    'STRIPE_PUBLISHABLE', 'pk_test_XM1d9ZdgN3EmNQrFAGaSbG9e')
STRIPE_SECRET = os.getenv('STRIPE_SECRET', 'sk_test_TT86LFyGyFQTGKlQ4kOEVrTc')

# Paypal environment variables
SITE_URL = 'http://127.0.0.1:8000'
PAYPAL_NOTIFY_URL = 'http://9fa1441c.ngrok.io'
PAYPAL_RECEIVER_EMAIL = 'liam.cafearo@protonmail.com'
