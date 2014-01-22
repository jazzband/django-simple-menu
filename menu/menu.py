from django.conf import settings

import traceback
import sys
import re

class Menu(object):
    """
    Menu is a class that generates menus

    It allows for multiple named menus, which can be accessed in your templates
    using the generate_menu template tag.

    Menus are loaded from the INSTALLED_APPS, inside a file named menus.py.
    This file should import the Menu & MenuItem classes and then call add_item:

        Menu.add_item("main", MenuItem("My item",
                                       reverse("myapp.views.myview"),
                                       weight=10))

    Note: You cannot have the same URL in a MenuItem in different
    Menus, but it is not enforced. If you do submenus will not work
    properly.
    """
    items = {}
    sorted = {}
    loaded = False

    @classmethod
    def add_item(c, name, item):
        """
        add_item adds MenuItems to the menu identified by 'name'
        """
        if isinstance(item, MenuItem):
            if name not in c.items:
                c.items[name] = []
            c.items[name].append(item)
            c.sorted[name] = False

    @classmethod
    def load_menus(c):
        """
        load_menus loops through INSTALLED_APPS and loads the menu.py
        files from them.
        """

        # we don't need to do this more than once
        if c.loaded == True:
            return

        # loop through our INSTALLED_APPS
        for app in settings.INSTALLED_APPS:
            # skip any django apps
            if re.match("django", app):
                continue

            menu_module = '%s.menus' % app
            try:
                __import__(menu_module, fromlist=["menu",])
            except ImportError:
                pass

        c.loaded = True

    @classmethod
    def sort_menus(c):
        """
        sort_menus goes through the items and sorts them based on
        their weight
        """
        for name in c.items:
            if c.sorted[name] != True:
                c.items[name].sort(cmp=lambda x,y: cmp(x.weight, y.weight))
                c.sorted[name] = True

    @classmethod
    def process(c, request, name=None):
        """
        process uses the current request to determine which menus
        should be visible, which are selected, etc.
        """
        # make sure we're loaded & sorted
        c.load_menus()
        c.sort_menus()

        if name is None:
            # special case, process all menus
            items = {}
            for name in c.items:
                items[name] = c.process(request, name)
            return items

        if name not in c.items:
            return []

        curitem = None
        for item in c.items[name]:
            item.process(request)
            if item.visible == True:
                item.selected = False
                if item.match_url(request):
                    if curitem is None or len(curitem.url) < len(item.url):
                        curitem = item

        if curitem is not None:
            curitem.selected = True

        # return only visible items
        visible = [
            item
            for item in c.items[name]
            if item.visible
        ]

        # determine if we should apply 'selected' to parents when one of their
        # children is the 'selected' menu
        if getattr(settings, 'MENU_SELECT_PARENTS', False):
            def is_child_selected(item):
                for child in item.children:
                    if child.selected or is_child_selected(child):
                        return True

            for item in visible:
                if is_child_selected(item):
                    item.selected = True

        return visible


class MenuItem(object):
    """
    MenuItem represents an item in a menu, possibly one that has a sub-
    menu (children).
    """

    def __init__(self, title, url, children=[], weight=1, check=None, 
                 visible=True, slug=None, exact_url=False, **kwargs):
        """
        MenuItem constructor

        title       either a string or a callable to be used for the title
        url         the url of the item
        children    an array of MenuItems that are sub menus to this item
                    this can also be a callable that generates an array
        weight      used to sort adjacent MenuItems
        check       a callable to determine if this item is visible
        slug        used to generate id's in the HTML, auto generated from
                    the title if left as None
        exact_url   normally we check if the url matches the request prefix
                    this requires an exact match if set

        All other keyword arguments passed into the MenuItem constructor are
        assigned to the MenuItem object as attributes so that they may be used
        in your templates. This allows you to attach arbitrary data and use it
        in which ever way suits your menus the best.
        """

        self.url = url
        self.title = title
        self._title = None
        self.visible = visible
        self.children = children
        self.children_sorted = False
        self.weight = weight
        self.check = check
        self.slug = slug
        self.exact_url = exact_url
        self.selected = False
        self.parent = None

        # merge our kwargs into our self
        for k in kwargs:
            setattr(self, k, kwargs[k])

        # if title is a callable store a reference to it for later
        # then we'll process it at runtime
        if callable(title):
            self.title = ""
            self._title = title

    def process(self, request):
        """
        process determines if this item should visible, if its selected, etc...
        """
        self.check_check(request)
        if not self.visible:
            return

        self.check_title(request)
        self.check_children(request)

        children = [
            kid
            for kid in self.children
            if kid.visible
        ]

        curitem = None
        for item in children:
            item.process(request)
            item.selected = False

            if item.match_url(request):
                if curitem is None or len(curitem.url) < len(item.url):
                    curitem = item

        if curitem is not None:
            curitem.selected = True

    def match_url(self, request):
        """
        match url determines if this is selected
        """
        matched = False
        if self.exact_url:
            if re.match("%s$" % (self.url,), request.path):
                matched = True
        elif re.match("%s" % self.url, request.path):
            matched = True
        return matched

    def check_children(self, request):
        if hasattr(self, '_children'):
            self.children = self._children(request)
        if callable(self.children):
            kids = self.children(request)
            self._children = self.children
            self.children = kids

        for kid in self.children:
            kid.parent = self

    def check_check(self, request):
        if callable(self.check):
            check = self.check(request)
            if check != True:
                self.visible = False
            else:
                self.visible = True

    def check_title(self, request):
        if callable(self._title):
            self.title = self._title(request)
        if self.slug is None:
            self.slug = re.sub(r'[^a-zA-Z0-9\-]+', '_', self.title.lower()).strip('_')
