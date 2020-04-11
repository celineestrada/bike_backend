from django.shortcuts import render


# from bike_backend.api import models


def hello_maps(request):
    # accidents = models.AccidentPoint.objects.all()
    # return render(request, 'index.html', {'accidents': accidents})
    return render(request, 'index.html', {})


def login(request):
    return render(request, 'login.html', {})

# def show_markers(request):
#    accidents = AccidentPoint.objects.all()
#    return render(request, 'index.html', {'accidents': accidents})
