import json

from django.contrib.auth import authenticate, login, logout
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import *
from .forms import *

# Create your views here.

# View to list minesweeps
def minesweepList(request):
	return render(
		request,
		'list_minesweep.html',
		context={
			'list': Minesweep.objects.all()
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