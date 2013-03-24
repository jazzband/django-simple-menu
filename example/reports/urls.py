from django.conf.urls.defaults import *

urlpatterns = patterns(
    'reports.views',

    url(r'staff/', 'staff'),
    url(r'superuser', 'superuser'),
    url(r'', 'index'),
)
