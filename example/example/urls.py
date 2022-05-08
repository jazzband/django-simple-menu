from django.urls import include, path, re_path
from django.conf.urls import patterns,  django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    re_path(r'^admin/', include(admin.site.urls)),

    path('accounts/login/', 'django.contrib.auth.views.login'),
    path('accounts/logout/', 'django.contrib.auth.views.logout'),

    re_path(r'^accounts/', include("accounts.urls")),
    re_path(r'^reports/', include("reports.urls")),
    re_path(r'', "accounts.views.index"),
)
