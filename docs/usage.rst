Using django-simple-menu
========================

Installation
------------

#. Install ``django-simple-menu`` using pip::

    pip install django-simple-menu

#. Add ``menu`` to your ``INSTALLED_APPS`` list in your settings

Usage Overview
--------------

``django-simple-menu`` lets you define multiple different menus that you can
access from within your templates. This way you can have a menu for your main
navigation, another menu for logged in users, another menu for anonymous users,
etc.

To define your menus you need to create a file named ``menu.py`` inside of the
app that you wish to hook menus up to. In the ``menu.py`` file you should
import the ``Menu`` and ``MenuItem`` classes from the ``menu`` package::

    from menu import Menu, MenuItem

The ``Menu`` class exposes a class method named ``add_item`` that accepts two
arguments; the menu name you want to add to, and the ``MenuItem`` you're going
to add.

The ``MenuItem`` class should be instantiated and passed to the ``add_item``
class method with the appropriate parameters. ``MenuItem`` accepts a wide
number of options to its constructor method, the majority of which are simply
attributes that become available in your templates when you're rendering out
the menus. The required arguments to MenuItem are the first two; the title of
the menu and the URL, and the keywords that affect menu generation are:

* The ``weight`` keyword argument affects sorting of the menu.
* The ``children`` keyword argument is either a list of ``MenuItem`` objects,
  or a callable which accepts the request object and returns a list.
* The ``check`` keyword argument is a callable that accepts the request object
  and returns ``True`` or ``False`` if the ``MenuItem`` should be visible for
  this request

For the full list of ``MenuItem`` options see the `menu __init__.py source file`_. 

Usage Example
-------------

Example::

    # Add two items to our main menu
    Menu.add_item("main", MenuItem("Tools",
                                   reverse("myapp.views.tools"),
                                   weight=10,
                                   icon="tools"))

    Menu.add_item("main", MenuItem("Reports",
                                   reverse("myapp.views.reports"),
                                   weight=20,
                                   icon="report"))


    # Define children for the my account menu
    myaccount_children = (
        MenuItem("Edit Profile",
                 reverse("accounts.views.editprofile"),
                 weight=10,
                 icon="user"),
        MenuItem("Admin",
                 reverse("admin:index"),
                 weight=80,
                 separator=True,
                 check=lambda request: request.user.is_superuser),
        MenuItem("Logout",
                 reverse("accounts.views.logout"),
                 weight=90,
                 separator=True,
                 icon="user"),
    )

    # Add a My Account item to our user menu
    Menu.add_item("user", MenuItem("My Account",
                                   reverse("accounts.views.myaccount"),
                                   weight=10,
                                   children=myaccount_children))


Once you have your menus defined you need to incorporate them into your
templates. This is done through the ``generate_menu`` template tag::

    {% import menu %}{% generate_menu %}

Once you call ``generate_menu`` all of your MenuItems will be evaluated and
the following items will be set in the context for you.

#. ``menus`` - This is an object that contains all of the lists of menus as
   attribute names::

       {% for item in menus.user %} ... {% endfor %}

#. ``selected_menu`` - This is the ``MenuItem`` object of the most specific
   URL match.
#. ``submenu`` - This is the submenu object of the most specific URL match.
#. ``has_submenu`` - This is ``True`` or ``False`` if the selected menu has
   children.


See the bootstrap-navbar.html file in the templates dir of the source code for
an example that renders menus for the `Twitter Bootstrap Navbar Component`_.
You can use it like::

    {% with menu=menus.main %}{% include "bootstrap-navbar.html" %}{% endwith %}

.. _menu __init__.py source file: https://github.com/fatbox/django-simple-menu/blob/master/menu/__init__.py
.. _Twitter Bootstrap Navbar Component: http://twitter.github.com/bootstrap/components.html#navbar
