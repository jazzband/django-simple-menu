#from django.conf.urls import patterns, include, url
from django.conf.urls import include, url
from django.contrib import admin
from accounts import views as acct_views
from django.contrib.auth import views as adm_views
admin.autodiscover()

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    url(r'^accounts/login/$', adm_views.login, name='django.contrib.auth.views.login'),
    url(r'^accounts/logout/$', adm_views.logout, name='django.contrib.auth.views.logout'),

    url(r'^accounts/', include("accounts.urls")),
    url(r'^reports/', include("reports.urls")),
    url(r'', acct_views.index),
]
