from __future__ import absolute_import, unicode_literals
from .base import *
import os

SECRET_KEY = os.environ['NERDHOUSESECRET']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['*'] 



try:
    from .local import *
except ImportError:
    pass
