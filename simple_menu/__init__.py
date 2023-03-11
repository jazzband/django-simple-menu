import sys

if sys.version_info < (3, 8):  # pragma: <3.8 cover
    from importlib_metadata import PackageNotFoundError, version
else:  # pragma: >=3.8 cover
    from importlib.metadata import PackageNotFoundError, version

from .menu import Menu, MenuItem

try:
    __version__ = version("django-simple-menu")
except PackageNotFoundError:
    # package is not installed
    __version__ = None

__url__ = 'https://github.com/jazzband/django-simple-menu'
