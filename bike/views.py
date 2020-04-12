from django.shortcuts import render
from .api.models import AccidentPoint
from .api.models import Hospital
from .api.models import Streetlight


def hello_maps(request):
    accidents = AccidentPoint.objects.all()
    hospitals = Hospital.objects.all()
    streetlights = Streetlight.objects.all()
    return render(request, 'index.html', {'accidents': accidents,
                                          'hospitals': hospitals,
                                          'streetlights': streetlights})


def login(request):
    return render(request, 'login.html', {})
