from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.db import models

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField()
    last_name = forms.CharField()

    class Meta:
        model = User
        fields = ['first_name',
                  'last_name',
                  'email',
                  'username',
                  'password1',
                  'password2']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields =['email',
                 'username']

class MapQueryForm(forms.Form):
    id = forms.IntegerField(required=False, widget=forms.HiddenInput())
    origin = forms.CharField(max_length=45, required=True)
    origin_lat = forms.FloatField(required=True)
    origin_lng = forms.FloatField(required=True)
    destination = forms.CharField(max_length=45, required=True)
    destination_lat = forms.FloatField(required=True)
    destination_lng = forms.FloatField(required=True)
    polyline = forms.CharField(max_length=510, required=True)
    score = forms.FloatField(required=True),
    name = forms.CharField(max_length=255, required=True)

