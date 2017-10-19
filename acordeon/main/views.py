from django.shortcuts import render

from .models import *
from .forms import AccordionForm

# Create your views here.
def index(request):
    return render(request, 'index.html')

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
