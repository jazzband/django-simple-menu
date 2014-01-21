import unittest

from django.conf import settings

from menu import Menu, MenuItem

settings.configure(
    INSTALLED_APPS=[],
    MENU_SELECT_PARENTS=False,
)

class MockRequest(object):
    def __init__(self, path):
        self.path = path

class MenuTests(unittest.TestCase):
    def test_select_parents(self):
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

        request = MockRequest('/parent2/kids2-1')
        Menu.process(request, 'test')
        self.assertEqual(Menu.items['test'][1].selected, True)
        self.assertEqual(Menu.items['test'][2].selected, False)
        self.assertEqual(Menu.items['test'][1].children[0].selected, True)

        request = MockRequest('/kids2-2')
        Menu.process(request, 'test')
        self.assertEqual(Menu.items['test'][1].selected, False)
        self.assertEqual(Menu.items['test'][2].selected, False)
        self.assertEqual(Menu.items['test'][1].children[1].selected, True)

        settings.MENU_SELECT_PARENTS = True
        request = MockRequest('/kids2-2')
        Menu.process(request, 'test')
        self.assertEqual(Menu.items['test'][1].selected, True)
        self.assertEqual(Menu.items['test'][2].selected, False)
        self.assertEqual(Menu.items['test'][1].children[1].selected, True)
