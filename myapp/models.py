# Define entities of the Web app.
# Models are translated into database tables automatically
from django.db import models
# from django.contrib.gis.db import models

# Create your models here.
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
    latitude = models.DecimalField(max_digits=20)
    longitude = models.DecimalField(max_digits=20)

class Hospital(models.Model):
    uniqueId = models.TextField(unique=True)
    name = models.CharField(max_length=256)
    street_address = models.CharField(max_length=256)
    zipcode = models.IntegerField(null=False)
    neighborhood = models.CharField(max_length=64)
    x_cord = models.DecimalField(max_digits=10)
    y_cord = models.DecimalField(max_digits=10)

class StreetLight(models.Model):
    uniqueId = models.TextField(unique=True)
    x_cord = models.DecimalField(max_digits=10)
    y_cord = models.DecimalField(max_digits=10)
