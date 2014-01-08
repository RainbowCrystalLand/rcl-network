from settings_base import *

# Since code is in a public repo, we encourage you to overwrite this
SECRET_KEY = '6@bltq%-qf&q6m**x3)ho(g2xprz4&hhs0omjaztp&iz)^gad8'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': '',                      # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': '',
        'PASSWORD': '',
        'HOST': '',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',                      # Set to empty string for default.
    }
}

# Set to override default admins to get error messages of this instace
# ADMINS = ()

# Set the Site to be used
# SITE_ID = 1  # production server
SITE_ID = 2  # local server
# SITE_ID = 3  # staging/testing server

# Uncomment to allow debugging features in local and testing servers
# DEBUG = SITE_ID != 1

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = ''
# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
STATIC_ROOT = ''

# Email settings
EMAIL_USE_TLS = True
EMAIL_HOST = ''
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_PORT = 587

SOUTH_TESTS_MIGRATE = False
