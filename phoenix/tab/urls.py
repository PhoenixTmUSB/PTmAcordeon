from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'^tab/$', tabList, name='tab-list'),
    url(r'^crear-tab/$', tabCreate, name='tab-create'),
    url(r'^crear-tab/(?P<container_id>[\w\-]+)$',
        tabCreate,
        name='tab-create'
        ),
    url(r'^editar-tab/(?P<tab_id>[\w\-]+)$', tabEdit, name='tab-edit'),
    url(r'^eliminar-tab/(?P<tab_id>[\w\-]+)$', tabDelete, name='tab-delete'),
    url(r'^eliminar-container/(?P<container_id>[\w\-]+)$',
        containerDelete,
        name='container-delete'
        ),
]
