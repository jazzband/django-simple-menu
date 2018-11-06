from django.conf.urls import *
from . import views

urlpatterns = [ 
    url(r'', views.index, name='reports.views.index'),
    url(r'staff/', views.staff, name='reports.views.staff'),
    url(r'superuser', views.superuser, name='reports.views.superuser'),
]
