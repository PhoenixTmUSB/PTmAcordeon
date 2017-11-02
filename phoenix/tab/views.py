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
            'list': TabContainer.objects.order_by('id'),
            # Tabs ordenadas por id
            'tabs': Tab.objects.order_by('id'),
            'accordionForm': AccordionForm,
            'minesweepForm': MinesweepForm,
            'tabForm': TabForm,
        }
    )


# View to create Tabs
def tabCreate(request, container_id=None):
    context = {}

    if request.method == 'POST':

        form = TabForm(request.POST)
        context['tabForm'] = form

        if form.is_valid():

            cleaned = form.cleaned_data
            numbertabs = cleaned['number_tabs']

            try:
                parent = TabContainer.objects.get(id=container_id)
                parent.children_amount += numbertabs
                parent.save()
            except ObjectDoesNotExist:
                parent = TabContainer.objects.create(
                    name=cleaned['title'],
                    children_amount=numbertabs
                )

            # Se hace un Objeto Tab y se asignan los fields arbitrariamente
            # Asignar el form.save() crea un solo elemento Tab
            for i in range(0, numbertabs):
                Tab(
                    parent=parent,
                    title=cleaned['title'],
                    title_style=cleaned['title_style'],
                    content=cleaned['content'],
                    content_style=cleaned['content_style'],
                    content_color=cleaned['content_color'],
                    width=cleaned['width'],
                    height=cleaned['height'],
                    border_style=cleaned['border_style'],
                    border_color=cleaned['border_color'],
                    border_radius=cleaned['border_radius'],
                    style=cleaned['style']
                ).save()

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
            container = TabContainer.objects.get(id=tab.parent.id)
        except ObjectDoesNotExist:
            raise ObjectDoesNotExist()

        container.children_amount -= 1
        container.save()
        tab.delete()
        if(container.children_amount == 0):
            container.delete()

    return redirect('tab:tab-list')
