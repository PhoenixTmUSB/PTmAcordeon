from django.shortcuts import render
from django.http import HttpResponse

from .models import *


def minesweep(request):
	context = {}
	lista = Minesweep.objects.all()
	context['tooltip'] = lista
	print('this we got')
	print(context)
	return HttpResponse("Hola Mundo")

def tooltip_demo(request):
    return render(request, 'tooltip_demo.html')
