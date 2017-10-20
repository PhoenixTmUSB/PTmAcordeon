import json
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse

from .models import *
from .forms import AccordionForm


def index(request):
    context = {}
    context['accordionForm'] = AccordionForm()
    return render(request, 'index.html', context)


def accordionList(request):
    a = Accordion.objects.all()
    context = {}
    context['list'] = a
    context['accordionForm'] = AccordionForm()
    return render(request, 'list_accordion.html', context)


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
