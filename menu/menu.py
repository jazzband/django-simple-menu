import warnings

from simple_menu.menu import *

warnings.warn(
    "Importing from 'menu' is deprecated. Import from 'simple_menu' instead. "
    "The old import will be removed in django-simple-menu v3, but no earlier "
    "than on 2024-04-01.",
    DeprecationWarning,
    stacklevel=2
)
