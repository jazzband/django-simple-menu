from django.core.urlresolvers import reverse

from menu import Menu, MenuItem

Menu.add_item("main", MenuItem("Accounts Index",
                               reverse("accounts.views.index")))

Menu.add_item("user", MenuItem("Login",
                               reverse('django.contrib.auth.views.login'),
                               check=lambda request: not request.user.is_authenticated()))
Menu.add_item("user", MenuItem("Logout",
                               reverse('django.contrib.auth.views.logout'),
                               check=lambda request: request.user.is_authenticated()))
Menu.add_item("user", MenuItem("Admin",
                               reverse("admin:index"),
                               separator=True,
                               check=lambda request: request.user.is_superuser))
