from django.shortcuts import render
from .api.models import AccidentPoint


def hello_maps(request):
    accidents = AccidentPoint.objects.all()
    return render(request, 'index.html', {'accidents': accidents})
    # return render(request, 'index.html', {})


def login(request):
    return render(request, 'login.html', {})

# def show_markers(request):
#    accidents = AccidentPoint.objects.all()
#    return render(request, 'index.html', {'accidents': accidents})
