from pkg_resources import get_distribution, DistributionNotFound
from .menu import Menu, MenuItem  # noqa

try:
    __version__ = get_distribution("django-simple-menu").version
except DistributionNotFound:
    # package is not installed
    __version__ = None

__url__ = 'https://github.com/jazzband/django-simple-menu'
