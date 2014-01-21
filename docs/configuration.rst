Configuring django-simple-menu
==============================
``django-simple-menu`` has some configuration options that can be configured
in your main `Django settings file`_.

MENU_SELECT_PARENTS
-------------------
**Default: ``False``**

``MENU_SELECT_PARENTS`` controls if parent menu items should automatically have
their ``selected`` property set to ``True`` if one of their children has its
``selected`` property set to ``True``.


.. _Django settings file: https://docs.djangoproject.com/en/dev/topics/settings/
