from django.core.urlresolvers import reverse

from menu import Menu, MenuItem

Menu.add_item("main", MenuItem("Reports Index",
                               reverse("reports.views.index")))

Menu.add_item("main", MenuItem("Staff Only",
                               reverse("reports.views.staff"),
                               check=lambda request: request.user.is_staff))

Menu.add_item("main", MenuItem("Superuser Only",
                               reverse("reports.views.superuser"),
                               check=lambda request: request.user.is_superuser))
