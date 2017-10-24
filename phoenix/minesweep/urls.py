from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'^minesweep/$', minesweep, name='minesweep-list'),
    url(r'^minesweep/tooltip-demo/$', tooltip_demo, name='tooltip-demo')
]