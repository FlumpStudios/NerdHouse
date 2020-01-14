from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '8nz9a66@rxt%^0htjm@smt8z1x!y964u$b@!8mjb8=$ubib2a+'

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['*'] 




try:
    from .local import *
except ImportError:
    pass
