from django.shortcuts import render
from .models import *


def index(request):
    return render(request, 'index.html')


def acordeon(request):
    a = Accordion.objects.all()
    context = {}
    context['list'] = a
    return render(request, 'acordeon.html', context)
