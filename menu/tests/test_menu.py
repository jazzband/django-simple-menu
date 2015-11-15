import unittest

from django.conf import settings
from django.template import Template, Context
from django.test import TestCase
from django.test.client import RequestFactory

from menu import Menu, MenuItem

class MenuTests(TestCase):
    def setUp(self):
        # allow the title of kids3-2 to be changed
        self.kids3_2_desired_title = None
        def kids3_2_title(request):
            if self.kids3_2_desired_title is not None:
                return "-".join([request.path, self.kids3_2_desired_title])
            return 'kids3-2'

        # hide kids2-2 whenever the request path ends with /hidden
        def kids2_2_check(request):
            if request.path.endswith('/hidden'):
                return False
            return True

        kids2 = [
            MenuItem("kids2-1", "/parent2/kids2-1", weight=999),
            MenuItem("kids2-2", "/kids2-2", check=kids2_2_check)
        ]
        kids3 = [
            MenuItem("kids3-1", "/parent3/kids3-1", children=[
              MenuItem("kids3-1-1", "/parent3/kids3-1/kid1", exact_url=True)
            ]),
            MenuItem(kids3_2_title, "/parent3/kids3-2")
        ]

        Menu.items = {}
        Menu.sorted = {}
        Menu.loaded = False
        Menu.add_item("test", MenuItem("Parent 1", "/parent1", weight=999))
        Menu.add_item("test", MenuItem("Parent 2", "/parent2", children=kids2))
        Menu.add_item("test", MenuItem("Parent 3", "/parent3", children=kids3))

        self.factory = RequestFactory()

    def test_exact_url(self):
        """
        Ensure that the exact_url setting works
        """
        # the extra stuff will still cause kids3-2 to be selected
        request = self.factory.get('/parent3/kids3-2/extra_stuff_here')
        Menu.process(request, 'test')
        self.assertEqual(Menu.items['test'][1].children[1].selected, True)

        # but here it won't, because exact_url is set
        request = self.factory.get('/parent3/kids3-1/kid1/extra_stuff_here')
        Menu.process(request, 'test')
        self.assertEqual(Menu.items['test'][1].children[0].children[0].selected, False)

    def test_callable_title(self):
        """
        Ensure callable titles work
        """
        self.kids3_2_desired_title = "fun"
        request = self.factory.get('/parent3')
        Menu.process(request, 'test')
        self.assertEqual(Menu.items['test'][1].children[1].title, "/parent3-fun")

    def test_checks(self):
        """
        Ensure checks on menus work
        """
        request = self.factory.get('/kids2-2/visible')
        Menu.process(request, 'test')
        self.assertEqual(len(Menu.items['test'][0].children), 2)

        request = self.factory.get('/kids2-2/hidden')
        Menu.process(request, 'test')
        self.assertEqual(len(Menu.items['test'][0].children), 1)

    def test_select_parents(self):
        """
        Ensure the MENU_SELECT_PARENTS setting works
        """
        settings.MENU_SELECT_PARENTS = False
        request = self.factory.get('/parent2/kids2-1')
        Menu.process(request, 'test')
        self.assertEqual(Menu.items['test'][0].selected, True)
        self.assertEqual(Menu.items['test'][0].children[1].selected, True)
        self.assertEqual(Menu.items['test'][1].selected, False)

        request = self.factory.get('/kids2-2')
        Menu.process(request, 'test')
        self.assertEqual(Menu.items['test'][0].selected, False)
        self.assertEqual(Menu.items['test'][0].children[0].selected, True)
        self.assertEqual(Menu.items['test'][1].selected, False)

        settings.MENU_SELECT_PARENTS = True
        request = self.factory.get('/kids2-2')
        Menu.process(request, 'test')
        self.assertEqual(Menu.items['test'][0].selected, True)
        self.assertEqual(Menu.items['test'][0].children[0].selected, True)
        self.assertEqual(Menu.items['test'][1].selected, False)

        request = self.factory.get('/parent3/kids3-1/kid1')
        Menu.process(request, 'test')
        self.assertEqual(Menu.items['test'][0].selected, False)
        self.assertEqual(Menu.items['test'][0].children[1].selected, False)
        self.assertEqual(Menu.items['test'][1].selected, True)
        self.assertEqual(Menu.items['test'][1].children[0].selected, True)
        self.assertEqual(Menu.items['test'][1].children[0].children[0].selected, True)
        self.assertEqual(Menu.items['test'][1].children[1].selected, False)
        self.assertEqual(Menu.items['test'][2].selected, False)

    def test_template_tag(self):
        """
        Ensure the templating works
        """
        request = self.factory.get('/parent3/kids3-1')
        out = Template(
            "{% load menu %}"
            "{% generate_menu %}"
            "{% for item in menus.test %}"
            "{{ item.title }},"
            "{% for child in item.children %}"
            "{{ child.title }},"
            "{% for grandchild in child.children %}"
            "{{ grandchild.title }},"
            "{% endfor %}"
            "{% endfor %}"
            "{% endfor %}"
        ).render(Context({
            'request': request,
        }))

        self.assertEqual(out, "Parent 2,kids2-2,kids2-1,Parent 3,kids3-1,kids3-1-1,kids3-2,Parent 1,")

    def test_template_tag_missing_attribute(self):
        """
        Missing attributes should not raise exceptions in templates
        """
        request = self.factory.get('/parent2/kids2-1')
        out = Template(
            "{% load menu %}"
            "{% generate_menu %}"
            "{% for item in menus.test %}"
            "{{ item.title }}{{ item.doesntexist }},"
            "{% endfor %}"
        ).render(Context({
            'request': request,
        }))

        self.assertEqual(out, "Parent 2,Parent 3,Parent 1,")

class MenuItemTests(TestCase):
    def test_kwargs(self):
        """
        MenuItems should accept arbitrary keyword args
        """
        item = MenuItem("test", "/test", arbitrary=True, dictionary={'a': 1})
        self.assertTrue(item.arbitrary)
        self.assertEqual(item.dictionary, {'a': 1})
        self.assertRaises(AttributeError, lambda: item.nope)
