import json
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from .models import *
from .forms import AccordionForm


# View to index
def index(request):
    return render(
        request,
        'index.html',
        context={
            'accordionForm': AccordionForm
        }
    )


# View to list accordions
def accordionList(request):
    return render(
        request,
        'list_accordion.html',
        context={
            'list': Accordion.objects.all(),
            'accordionForm': AccordionForm,
        }
    )


# View to create accordions
def accordionCreate(request):
    context = {}

    if request.method == 'POST':
        form = AccordionForm(request.POST)
        context['accordionForm'] = form

        if form.is_valid():
            panel_nro = form.cleaned_data['panels']
            parent = form.save()

            for i in range(0, panel_nro):
                Accordion(
                    title='Panel hijo',
                    parent=parent
                ).save()

            return HttpResponse(
                content=json.dumps({"redirectTo": reverse('main:accordion-list')}),
                content_type='application/json',
                status=200
            )

        # Error in form.
        return HttpResponse(json.dumps(form.errors), status=400)
    else:
        context['accordionForm'] = AccordionForm()

    return render(request, 'index.html', context, status=400)


# View to delete accordions
def accordionEdit(request, accordion_id):
    # Initialize context and search for accordion to edit
    try:
        accordion = Accordion.all_objects.get(accordion_id=accordion_id)
    except ObjectDoesNotExist:
        raise ObjectDoesNotExist()

    context = {
        'accordionForm': AccordionForm(),
        'accordion': accordion
    }

    if request.method == 'POST':
        form = AccordionForm(request.POST or None, instance=accordion)
        context['accordionFormEdit'] = form

        if form.is_valid():
            panel_nro = form.cleaned_data['panels']
            parent = form.save()

            for i in range(0, panel_nro):
                Accordion(
                    title='Panel hijo',
                    parent=parent
                ).save()
    else:
        context['accordionFormEdit'] = AccordionForm(instance=accordion)

    return render(request, 'edit_accordion.html', context)


# View to delete accordions
def accordionDelete(request, accordion_id):
    # Get accordion to delete and delete it
    if request.method == 'GET':
        try:
            accordion = Accordion.all_objects.get(accordion_id=accordion_id)
        except ObjectDoesNotExist:
            raise ObjectDoesNotExist()
        accordion.delete()

    return redirect('main:accordion-list')
