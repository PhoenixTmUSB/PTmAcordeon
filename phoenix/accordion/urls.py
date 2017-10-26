from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'^$', index, name='accordion-index'),
    url(r'^acordeon/$', accordionList, name='accordion-list'),
    url(r'^crear-acordeon/$', accordionCreate, name='accordion-create'),
    url(r'^editar-acordeon/(?P<accordion_id>[\w\-]+)$', accordionEdit, name='accordion-edit'),
    url(r'^eliminar-acordeon/(?P<accordion_id>[\w\-]+)$', accordionDelete, name='accordion-delete'),
    url(r'^ajax_log_in/$', ajax_log_in_view, name='ajax_log_in_view'),
    url(r'^logout/$', logout_user, name='logout'),
]
