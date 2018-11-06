from django.conf.urls import *
from . import views

urlpatterns = [
    url(r'', views.index, name='accounts.views.index'),
    url(r'profile/', views.profile, name='accounts.views.profile'),
]
