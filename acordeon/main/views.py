from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def acordeon(request):
    return render(request, 'acordeon.html')
