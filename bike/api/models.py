# Define entities of the Web app.
# Models are translated into database tables automatically
from django.contrib.gis.db import models
from django.contrib.gis import admin
from django.contrib.auth import get_user_model
# from maps.forms import UserCreationForm
# from maps.forms import CustomUserChangeForm
from django.contrib.gis.geos import Point
from datetime import datetime


# Create your models here.

class AccidentPoint(models.Model):

    class Meta:
        app_label = 'api'

    #uniqueId = models.IntegerField(unique=True)
    # dispatch_ts = models.DateTimeField()
    mode_type = models.CharField(max_length=10, null=False)
    location_type = models.CharField(max_length=45, null=False)
    street = models.CharField(max_length=45, null=False)
    xstreet1 = models.CharField(max_length=45, null=False)
    xstreet2 = models.CharField(max_length=45, null=False)
    # x_cord = models.DecimalField(max_digits=10)
    # y_cord = models.DecimalField(max_digits=10)
    latitude = models.FloatField(null=False)
    longitude = models.FloatField(null=False)
    # point = models.PointField(default='POINT(0 0', srid=4236)
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)

    # Rather than storing lat and long directly into the database, store it in properties
    # This is a property decorator to access it without calling a function

    #
    # @property
    # def longitude(self):
    #     return self.point[0]
    #
    # def latitude(self):
    #     return self.point[1]
    #

    def __str__(self):
        return str(self.id)


class Hospital(models.Model):

    class Meta:
        app_label = 'api'

    x_cord = models.FloatField(null=False)
    y_cord = models.FloatField(null=False)
    #uniqueId = models.IntegerField(unique=True)
    name = models.CharField(max_length=100, null=False)
    address = models.CharField(max_length=100, null=False)
    zipcode = models.IntegerField(null=False)
    contact = models.CharField(max_length=100, null=False)
    phone = models.CharField(max_length=15, null=False)
    latitude = models.FloatField(null=False)
    longitude = models.FloatField(null=False)
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)


class Streetlight(models.Model):

    class Meta:
        app_label = 'api'

    #uniqueId = models.IntegerField(unique=True)
    type = models.CharField(max_length=45, null=False)
    latitude = models.FloatField(null=False)
    longitude = models.FloatField(null=False)
    # x_cord = models.DecimalField(max_digits=10)
    # y_cord = models.DecimalField(max_digits=10)
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)
