from settings_base import *

# Since code is in a public repo, we encourage you to overwrite this
SECRET_KEY = '6@bltq%-qf&q6m**x3)ho(g2xprz4&hhs0omjaztp&iz)^gad8'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'rcl_network',                      # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': '',
        'PASSWORD': '',
        'HOST': '',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',                      # Set to empty string for default.
    }
}

# Our custom User model (replaces Django auth User)
AUTH_USER_MODEL = 'users.User'