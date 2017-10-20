from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'^$', index, name='accordion-index'),
    url(r'^acordeon/$', accordionList, name='accordion-list'),
    url(r'^crear-acordeon/$', accordionCreate, name='accordion-create'),
]
