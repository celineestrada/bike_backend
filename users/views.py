from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserRegisterForm, UserUpdateForm, MapQueryForm
from django.contrib import messages
from django.contrib.auth.models import User



from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin



def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to login!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


def delete(request, username):
    user = User.objects.get(username=username)
    user.delete()
    return redirect('deleted')

def update(request):
    if request.method == 'POST':
     u_form = UserUpdateForm(request.POST, instance=request.user)
     if u_form.is_valid():
         u_form.save()
         messages.success(request, f'Your account has been updated')
         return redirect('login')
    else:
        u_form = UserUpdateForm(instance=request.user)
    return render(request, 'users/update.html', {'u_form': u_form})







