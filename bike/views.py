from django.shortcuts import render
from .api.models import AccidentPoint
from django.contrib.auth import login,authenticate
from django.contrib.auth.forms import UserCreationForm


def hello_maps(request):
    accidents = AccidentPoint.objects.all()
    return render(request, 'index.html', {'accidents': accidents})
    # return render(request, 'index.html', {})


def login(request):
    form = UserCreationForm()
    return render(request, 'login.html', {"form":form})





    # def register(request):
    #     if request.method == 'POST':
    #         form = UserRegisterForm(request.POST)
    #         if form.is_valid():
    #             form.save()
    #             username = form.cleaned_data.get('username')
    #             messages.success(request, f'Your account has been created! You are now able to login!')
    #             return redirect('login')


# def show_markers(request):
#    accidents = AccidentPoint.objects.all()
#    return render(request, 'index.html', {'accidents': accidents})
