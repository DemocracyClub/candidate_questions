from .base import *


DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Sym Roe', 'sym@democracyclub.org.uk'),
)

MANAGERS = ADMINS


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'q_and_a',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}
