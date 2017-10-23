from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'^minesweep/$', minesweepList, name='minesweep-list'),
    url(r'^crear-minesweep/$', minesweepCreate, name='minesweep-create'),    
]