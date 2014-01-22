import unittest

from django.conf import settings
from django.test import TestCase
from django.test.client import RequestFactory

from menu import Menu, MenuItem

class MenuTests(TestCase):
    def setUp(self):
        kids2 = [
            MenuItem("kids2-1", "/parent2/kids2-1"),
            MenuItem("kids2-2", "/kids2-2")
        ]
        kids3 = [
            MenuItem("kids3-1", "/parent3/kids3-1")
        ]

        Menu.add_item("test", MenuItem("Parent 1", "/parent1"))
        Menu.add_item("test", MenuItem("Parent 2", "/parent2", children=kids2))
        Menu.add_item("test", MenuItem("Parent 3", "/parent3", children=kids3))

        self.factory = RequestFactory()

    def test_select_parents(self):
        request = self.factory.get('/parent2/kids2-1')
        Menu.process(request, 'test')
        self.assertEqual(Menu.items['test'][1].selected, True)
        self.assertEqual(Menu.items['test'][2].selected, False)
        self.assertEqual(Menu.items['test'][1].children[0].selected, True)

        request = self.factory.get('/kids2-2')
        Menu.process(request, 'test')
        self.assertEqual(Menu.items['test'][1].selected, False)
        self.assertEqual(Menu.items['test'][2].selected, False)
        self.assertEqual(Menu.items['test'][1].children[1].selected, True)

        settings.MENU_SELECT_PARENTS = True
        request = self.factory.get('/kids2-2')
        Menu.process(request, 'test')
        self.assertEqual(Menu.items['test'][1].selected, True)
        self.assertEqual(Menu.items['test'][2].selected, False)
        self.assertEqual(Menu.items['test'][1].children[1].selected, True)
