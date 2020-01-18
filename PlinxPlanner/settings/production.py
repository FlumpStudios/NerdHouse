from __future__ import absolute_import, unicode_literals
from .base import *
import os

env = os.environ.copy()
SECRET_KEY = '8nz9a66@rxt%^0htjm@smt8z1x!y964u$b@!8mjb8=$ubib2a+'

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
