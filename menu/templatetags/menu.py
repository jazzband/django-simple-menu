import warnings

from simple_menu.templatetags.simple_menu import *

warnings.warn(
    "Loading from 'menu' is deprecated. Use '{% load simple_menu %}' instead. "
    "The old template library will be removed in django-simple-menu v3, but "
    "no earlier than on 2024-04-01.",
    DeprecationWarning,
    stacklevel=2
)
