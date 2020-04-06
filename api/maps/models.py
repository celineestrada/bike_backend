# Define entities of the Web app.
# Models are translated into database tables automatically
from django.contrib.gis.db import models
from django.contrib.gis.goes import Point

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
    updated_at = model.DateTimeField(auto_now=True)

class StreetLight(models.Model):
    uniqueId = models.TextField(unique=True)
    x_cord = models.DecimalField(max_digits=10)
    y_cord = models.DecimalField(max_digits=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = model.DateTimeField(auto_now=True)
