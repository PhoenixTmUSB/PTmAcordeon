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
            form.save()

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


# View to delete acordions
def accordionEdit(request, accordion_id):
    # Initialize context and search for accordion to edit
    context = {}
    accordion = get_object_or_404(Accordion, accordion_id=accordion_id)

    if request.method == 'POST':
        form = AccordionForm(request.POST)
        context['accordionForm'] = form

        if form.is_valid():
            form.save()

        return HttpResponse(
            content=json.dumps({"redirectTo": reverse('main:accordion-list')}),
            content_type='application/json',
            status=200
        )

        # Error in form.
        return HttpResponse(json.dumps(form.errors), status=400)
    else:
        
        context['accordionForm'] = AccordionForm(instance=accordion)

    return render(request, 'edit_accordion.html', context, status=400)


# View to delete accordions
def accordionDelete(request, accordion_id):
    # Get accordion to delete and delete it
    if request.method == 'GET':
        accordion = get_object_or_404(Accordion, accordion_id=accordion_id)
        accordion.delete()

    return redirect('main:accordion-list')
