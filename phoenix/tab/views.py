import json

from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse

from .models import *
from .forms import *

from accordion.forms import AccordionForm
from minesweep.forms import MinesweepForm

# Create your views here.

def tabList(request):
    return render(
    	request,
    	'list_tab.html',
        context={
        	'list': Tab.objects.all(),
            'accordionForm': AccordionForm,
            'minesweepForm': MinesweepForm,
            'tabForm': TabForm,
        }    	
    )

# View to create Tabs
def tabCreate(request):
    context = {}

    if request.method == 'POST':
        form = TabForm(request.POST)
        context['tabForm'] = form

        if form.is_valid():
            form.save()
            return HttpResponse(
                content=json.dumps({"redirectTo": reverse('tab:tab-list')}),
                content_type='application/json',
                status=200
            )

        # Error in form.
        return HttpResponse(json.dumps(form.errors), status=400)
    else:
        context['tabForm'] = TabForm()

    return render(request, 'index.html', context, status=400)    
