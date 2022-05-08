Installing django-simple-menu
=============================

#. Install ``django-simple-menu`` using pip::

    pip install django-simple-menu

#. Add ``menu`` to your ``INSTALLED_APPS`` list in your settings

#. ``django-simple-menu`` requires that the ``request`` object be available in
   the context when you call the ``{% generate_menu %}`` template tag. This
   means that you need to ensure that your ``TEMPLATE_CONTEXT_PROCESSORS``
   setting includes ``django.core.context_processors.request``, which it
   doesn't by default.
