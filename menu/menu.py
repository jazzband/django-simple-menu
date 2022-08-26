import warnings

from simple_menu.menu import *

warnings.warn(
    "Importing from 'menu' will be removed in django-simple-menu v2.3 and/or "
    "v3.0. Use imports from 'simple_menu' package instead.",
    DeprecationWarning,
    stacklevel=2
)
