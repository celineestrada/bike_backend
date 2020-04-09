# Define entities of the Web app.
# Models are translated into database tables automatically
from django.contrib.gis.db import models
from django.contrib.gis import admin
from django.contrib.auth import get_user_model
from .forms import UserCreationForm
from .forms import CustomUserChangeForm
from django.contrib.gis.geos import Point
from datetime import datetime


# Create your models here.
class CustomUserAdmin(admin.OSMGeoAdmin):
    model = get_user_model()
    add_form = UserCreationForm
    form = CustomUserChangeForm

    list_display = ['email', 'last_name', 'first_name']
    readonly_fields = ['last_login', 'date_joined']

    def get_form(self, request, obj=None, **kwargs):
        """
        Use special form during user creation.

        Override get_form method in the same manner as django.contrib.auth.admin.UserAdmin does.
        """
        defaults = {}
        if obj is None:
            defaults['form'] = self.add_form
        defaults.update(kwargs)
        return super().get_form(request, obj, **defaults)


admin.site.register(get_user_model(), CustomUserAdmin)


class AccidentPoint(models.Model):
    uniqueId = models.TextField(unique=True)
    dispatch_ts = models.DateTimeField()
    mode_type = models.CharField(max_length=4)
    location_type = models.CharField(max_length=20)
    street = models.CharField(max_length=50)
    xstreet1 = models.CharField(max_length=50)
    xstreet2 = models.CharField(max_length=50)
    x_cord = models.DecimalField(max_digits=10)
    y_cord = models.DecimalField(max_digits=10)
    point = models.PointField(default='POINT(0 0', srid=4236)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Rather than storing lat and long directly into the database, store it in properties
    # This is a property decorator to access it without calling a function
    @property
    def longitude(self):
        return self.point[0]

    def latitude(self):
        return self.point[1]


class Hospital(models.Model):
    uniqueId = models.TextField(unique=True)
    name = models.CharField(max_length=256)
    street_address = models.CharField(max_length=256)
    zipcode = models.IntegerField(null=False)
    neighborhood = models.CharField(max_length=64)
    x_cord = models.DecimalField(max_digits=10)
    y_cord = models.DecimalField(max_digits=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Streetlight(models.Model):
    uniqueId = models.TextField(unique=True)
    x_cord = models.DecimalField(max_digits=10)
    y_cord = models.DecimalField(max_digits=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
