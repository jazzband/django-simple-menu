from django.core.urlresolvers import reverse

from menu import Menu, MenuItem

def profile_title(request):
    """
    Return a personalized title for our profile menu item
    """
    # we don't need to check if the user is authenticated because our menu
    # item will have a check that does that for us
    name = request.user.get_full_name() or request.user

    return "%s's Profile" % name

Menu.add_item("main", MenuItem("Accounts Index",
                               reverse("accounts.views.index")))

# this item will be shown to users who are not logged in
Menu.add_item("user", MenuItem("Login",
                               reverse('django.contrib.auth.views.login'),
                               check=lambda request: not request.user.is_authenticated()))

# this will only be shown to logged in users and also demonstrates how to use
# a callable for the title to return a customized title for each request
Menu.add_item("user", MenuItem(profile_title,
                               reverse('accounts.views.profile'),
                               check=lambda request: request.user.is_authenticated()))
Menu.add_item("user", MenuItem("Logout",
                               reverse('django.contrib.auth.views.logout'),
                               check=lambda request: request.user.is_authenticated()))

# this only shows to superusers
Menu.add_item("user", MenuItem("Admin",
                               reverse("admin:index"),
                               separator=True,
                               check=lambda request: request.user.is_superuser))
