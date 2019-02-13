Example Project for django-simple-menu
======================================

This is a complete example project for django-simple-menu that can be quickly
used to evaluate if django-simple-menu is right for you.

Setting up
----------
Use sqlite3 instead of pysqilte as it does not work with python it will not work
And do not have to install sqlite3

To setup the project you need to create a new virtualenv directory and install
the dependencies listed in the requirements file::

    virtualenv testenv
    source testenv/bin/activate
    pip install -r requirements.txt

Next setup the Django instance::

    python manage.py migrate 
    python manage.py makemigrations

And finally run the project::

    python manage.py runserver

Once you access the project at http://127.0.0.1:8000 you will see a menu that
will change depending on if you're logged in, logged in as a staff member or
logged in as a superuser. To fully see the menu system in action you will need
to login to the Django admin and create two new users (one just a staff member
and the other a regular user, you already have a superuser from the syncdb
call) and then login with all three of them to compare the resulting menus.
