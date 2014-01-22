import os

TEST_DIR = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'tests')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}

INSTALLED_APPS = [
    'menu'
]

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(TEST_DIR, 'static')

TEMPLATE_DIRS = (
    os.path.join(TEST_DIR, 'test_templates'),
)

SECRET_KEY = "testing-menus-is-so-much-fun"

