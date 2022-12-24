from django.shortcuts import render
from core.models import Car

def index(request):
    context = {
        'cars': Car.objects.all(),
    }
    return render(request, 'core/index.html', context)

def test(request):
    context = {}
    return render(request, 'core/test.html', context)
