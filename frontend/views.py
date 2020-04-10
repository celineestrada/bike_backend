from django.shortcuts import render


def hello_maps(request):
    return render(request, 'index.html', {})


def login(request):
    return render(request, 'login.html', {})
