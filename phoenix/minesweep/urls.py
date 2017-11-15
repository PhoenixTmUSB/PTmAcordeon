from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'^minesweep/$', minesweepList, name='minesweep-list'),
    url(r'^crear-minesweep/$', minesweepCreate, name='minesweep-create'),
    url(r'^editar-minesweep/(?P<minesweep_id>[\w\-]+)$', minesweepEdit, name='minesweep-edit'),
    url(r'^eliminar-minesweep/(?P<minesweep_id>[\w\-]+)$', minesweepDelete, name='minesweep-delete'),
    #url(r'^minesweep/tooltip-demo/$', tooltip_demo, name='tooltip-demo')
]