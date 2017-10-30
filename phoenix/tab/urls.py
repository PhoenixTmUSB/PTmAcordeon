from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'^tab/$', tabList, name='tab-list'),
    url(r'^crear-tab/$', tabCreate, name='tab-create'),    
]