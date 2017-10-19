from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.shortcuts import render, redirect

from .models import *


# Create your views here.
def index(request):
    return render(request, 'index.html')

def acordeon(request):
    a = Accordion.objects.all()
    context = {}
    context['list'] = a
    return render(request, 'acordeon.html', context)


## Inicia sesión del usuario por ajax
def ajax_log_in_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return JsonResponse({'autenticado': 1})
    else:
        return JsonResponse({'autenticado': 0})


## Cierra la sesión de un usuario y lo redirige al home
def logout_user(request):
    logout(request)
    return redirect(index)
