from django.conf.urls import *

urlpatterns = patterns(
    'accounts.views',

    url(r'profile/', 'profile'),
    url(r'', 'index')
)
