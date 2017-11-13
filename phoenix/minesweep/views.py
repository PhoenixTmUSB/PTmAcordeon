import json

from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse

from .models import *
from .forms import *

from accordion.forms import AccordionForm
from tab.forms import TabForm


# View to list minesweeps
def minesweepList(request):
    return render(
        request,
        'list_minesweep.html',
        context={
            'list': Minesweep.objects.all(),
            'accordionForm': AccordionForm,
            'minesweepForm': MinesweepForm,
            'tabForm': TabForm,
        }
    )


# View to create minesweeps
def minesweepCreate(request):
    context = {}

    if request.method == 'POST':
        form = MinesweepForm(request.POST)
        context['minesweepForm'] = form

        if form.is_valid():
            form.save()
            return HttpResponse(
                content=json.dumps({"redirectTo": reverse('minesweep:minesweep-list')}),
                content_type='application/json',
                status=200
            )

        # Error in form.
        return HttpResponse(json.dumps(form.errors), status=400)
    else:
        context['minesweepForm'] = MinesweepForm()

    return render(request, 'index.html', context, status=400)


# View to edit minesweeps
def minesweepEdit(request, minesweep_id):
    # Initialize context and search for minesweep to edit
    try:
        minesweep = Minesweep.objects.get(minesweep_id=minesweep_id)
    except ObjectDoesNotExist:
        raise ObjectDoesNotExist()

    context = {
        'minesweepForm': MinesweepForm(),
        'minesweep': minesweep
    }

    if request.method == 'POST':
        form = MinesweepForm(request.POST or None, instance=minesweep)
        context['minesweepFormEdit'] = form

        if form.is_valid():
            form.save()
    else:
        context['minesweepFormEdit'] = MinesweepForm(instance=minesweep)

    return render(request, 'edit_minesweep.html', context)


# View to delete minesweeps
def minesweepDelete(request, minesweep_id):
    # Get accordion to delete and delete it
    if request.method == 'GET':
        try:
            minesweep = Minesweep.objects.get(minesweep_id=minesweep_id)
        except ObjectDoesNotExist:
            raise ObjectDoesNotExist()
        minesweep.delete()

    return redirect('minesweep:minesweep-list')
