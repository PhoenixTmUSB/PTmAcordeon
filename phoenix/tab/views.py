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

# View to delete tabs
def tabEdit(request, tab_id):
    # Initialize context and search for tab to edit
    try:
        tab = Tab.objects.get(tab_id=tab_id)
    except ObjectDoesNotExist:
        raise ObjectDoesNotExist()

    context = {
        'tabForm': TabForm(),
        'tab': tab
    }

    if request.method == 'POST':
        form = TabForm(request.POST or None, instance=tab)
        context['tabFormEdit'] = form

        if form.is_valid():
            form.save()
    else:
        context['tabFormEdit'] = TabForm(instance=tab)

    return render(request, 'edit_tab.html', context)

# View to delete tabs
def tabDelete(request, tab_id):
    # Get tab to delete and delete it
    if request.method == 'GET':
        try:
            tab = Tab.objects.get(tab_id=tab_id)
        except ObjectDoesNotExist:
            raise ObjectDoesNotExist()
        tab.delete()

    return redirect('tab:tab-list')    