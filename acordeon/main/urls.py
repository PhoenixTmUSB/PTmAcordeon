from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^acordeon/$', acordeon, name='acordeon'),
    url(r'^ajax_log_in/$', ajax_log_in_view, name='ajax_log_in_view'),
    url(r'^logout/$', logout_user, name='logout'),

]
