from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.shortcuts import render, redirect

from .forms import AccordionForm
from .models import *


## Home, vista inicial que ven los usuarios
def index(request):
    return render(request, 'index.html')


## Vista encargada de renderizar el acordeón al usuario
def acordeon(request):
    a = Accordion.objects.all()
    context = {}
    context['list'] = a
    return render(request, 'acordeon.html', context)


def crear_acordeon(request):
    if request.method == 'POST':
        form = AccordionForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'index.html')
    else:
        form = AccordionForm()
    return render(request, 'crear_acordeon.html', {'form': form})


# Inicia sesión del usuario por ajax
def ajax_log_in_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return JsonResponse({'autenticado': 1})
    else:
        return JsonResponse({'autenticado': 0})


# Cierra la sesión de un usuario y lo redirige al home
def logout_user(request):
    logout(request)
    return redirect(index)
