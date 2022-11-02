===================================
django-simple-menu |latest-version|
===================================

|jazzband| |build-status| |coverage| |docs| |python-support| |django-support|

.. |latest-version| image:: https://img.shields.io/pypi/v/django-simple-menu.svg
   :target: https://pypi.python.org/pypi/django-simple-menu
   :alt: Latest version on PyPI

.. |jazzband| image:: https://jazzband.co/static/img/badge.svg
   :target: https://jazzband.co/
   :alt: Jazzband

.. |build-status| image:: https://github.com/jazzband/django-simple-menu/actions/workflows/test.yml/badge.svg
   :target: https://github.com/jazzband/django-simple-menu/actions
   :alt: Build Status

.. |coverage| image:: https://img.shields.io/codecov/c/github/jazzband/django-simple-menu.svg
   :target: https://codecov.io/github/jazzband/django-simple-menu
   :alt: Test coverage status

.. |docs| image:: https://img.shields.io/readthedocs/django-simple-menu/latest.svg
   :target: https://django-simple-menu.readthedocs.io/
   :alt: Documentation status

.. |python-support| image:: https://img.shields.io/pypi/pyversions/django-simple-menu
   :target: https://pypi.python.org/pypi/django-simple-menu
   :alt: Supported Python versions

.. |django-support| image:: https://img.shields.io/pypi/djversions/django-simple-menu
   :target: https://pypi.org/project/django-simple-menu
   :alt: Supported Django versions

``django-simple-menu`` is an entirely code based menu system, because, who
really wants to define their menus inside Django Admin?..

It's simple to use, yet provides enough flexibility to provide unlimited
children menus, per-request generation and checking of menu items, badges,
and more.


Quickstart
----------

**Requirements:** Python 3.6+, Django 3.2+

1. Install the ``django-simple-menu`` package.

2. Add ``simple_menu`` to your ``INSTALLED_APPS``.

   - please ensure that you have ``django.template.context_processors.request``
     listed under ``TEMPLATES[...]["OPTIONS"]["context_processors"]``.

3. Create ``menus.py`` inside each app you want to create a menu for and define
   said menus using the ``Menu`` and ``MenuItem`` classes you can import from
   the ``simple_menu`` package.

4. In your templates, load the template tags (``{% load simple_menu %}``) and
   call ``{% generate_menu %}`` inside a block. Your context will be populated
   with a new object named ``menus``. You can now iterate over it to render your
   menus.

To quickly see ``django-simple-menu`` in action, check out the
`example project`_.

.. _example project: https://github.com/jazzband/django-simple-menu/tree/master/example


More
----

Full documentation, including installation and configuration instructions, is
available at https://django-simple-menu.readthedocs.io/.

``django-simple-menu`` is released under the *BSD 2-Clause "Simplified" License*.
If you like it, please consider contributing!

``django-simple-menu`` was originally created by
Evan Borgstom <evan@borgstrom.ca> and was further developed by many
contributors_.

.. _contributors: https://github.com/jazzband/django-simple-menu/graphs/contributors
