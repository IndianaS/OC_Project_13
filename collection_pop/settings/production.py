from. import *
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration


ALLOWED_HOSTS = ['127.0.0.1', '192.168.1.42', 'collectionpop.fr']
DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'collection_pop',
        'USER': 'postgres',
        'PASSWORD': os.getenv('postgresql_password'),
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

sentry_sdk.init(
    dsn="https://3399934128f24c26bc98e7f74050e73e@o396835.ingest.sentry.io/5250733",
    integrations=[DjangoIntegration()],

    # If you wish to associate users to errors (assuming you are using
    # django.contrib.auth) you may enable sending PII data.
    send_default_pii=True
)
