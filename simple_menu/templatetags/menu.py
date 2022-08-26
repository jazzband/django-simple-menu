import warnings

from simple_menu.templatetags.simple_menu import *

warnings.warn(
    "The 'menu' template library will be removed in django-simple-menu v2.3 "
    "and/or v3.0. Use '{% load simple_menu %}' instead.",
    DeprecationWarning,
    stacklevel=2
)
