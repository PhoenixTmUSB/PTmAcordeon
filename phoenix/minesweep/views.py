from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def minesweep(request):
	context = {}
	lista = Minesweep.objects.all()
	context['tooltip'] = lista
	print('this we got')
	print(context)
	return HttpResponse("Hola Mundo")
