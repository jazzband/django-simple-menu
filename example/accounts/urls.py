from django.conf.urls.defaults import *

urlpatterns = patterns(
    'accounts.views',

    url(r'profile/', 'profile'),
    url(r'', 'index')
)
