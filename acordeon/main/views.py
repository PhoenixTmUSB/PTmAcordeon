from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    return render(request, 'index.html')

def acordeon(request):
    a = Accordion.objects.all()
    context = {}
    context['list'] = a
    return render(request, 'acordeon.html', context)

def crear_acordeon(request):
    return render(request, 'crear_acordeon.html')
