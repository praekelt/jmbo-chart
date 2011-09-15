import os

DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
    }
}

ROOT_URLCONF = 'chart.urls'

INSTALLED_APPS = (
    # jmbo required apps
    'category',
    'photologue',
    'secretballot',

    # elective apps
    'publisher',
    'jmbo',
    'category',
    'music',
    'chart',

    # django required apps
    'django.contrib.auth',
    'django.contrib.admin',
    'django.contrib.contenttypes',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
)


CKEDITOR_MEDIA_PREFIX = '/media/ckeditor/'

SITE_ID = 1
