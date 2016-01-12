Simple Django Menus
===================

.. image:: https://img.shields.io/travis/borgstrom/django-simple-menu.svg
           :target: https://travis-ci.org/borgstrom/django-simple-menu

.. image:: https://img.shields.io/codecov/c/github/borgstrom/django-simple-menu.svg
           :target: https://codecov.io/github/borgstrom/django-simple-menu

.. image:: https://img.shields.io/pypi/v/django-simple-menu.svg
           :target: https://pypi.python.org/pypi/django-simple-menu
           :alt: Latest PyPI version

.. image:: https://img.shields.io/pypi/dm/django-simple-menu.svg
           :target: https://pypi.python.org/pypi/django-simple-menu
           :alt: Number of PyPI downloads

django-simple-menu is an entirely code based menu system, because, who really wants to define their
menus in the django admin...

It's simple to use, yet provides enough flexibility to provide unlimited children menus, per-request
generation and checking of menu items, badges, and more.


Quickstart
----------

Using django-simple-menu is easy.

Install ``django-simple-menu`` in your virtualenv and then add ``menu`` to your ``INSTALLED_APPS``.
Please ensure that you have ``django.core.context_processors.request`` listed in the
``TEMPLATE_CONTEXT_PROCESSORS`` setting.

For each of your own apps that you want to expose a menu create a new file named ``menus.py`` and
define your menus using the ``Menu`` and ``MenuItem`` classes.

In a template you want to render a menu first ``{% load menu %}`` then inside a block call
``{% generate_menu %}`` and a new varaible named ``menus`` will be added to the context.  You can
now iterate over this ``menus`` object to render your menus.

To quickly see everything in action and evaluate django-simple-menut please check out the
`example project`_.

.. _example project: https://github.com/borgstrom/django-simple-menu/tree/master/example


Documentation
-------------

The full documentation is located in the docs directory and can be viewed at:

https://django-simple-menu.readthedocs.org


Requirements
------------

Django 1.6+
