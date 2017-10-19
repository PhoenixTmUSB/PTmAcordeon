from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^acordeon/$', acordeon, name='acordeon'),
    url(r'^crear_acordeon/$', crear_acordeon, name='crear_acordeon'),
]
