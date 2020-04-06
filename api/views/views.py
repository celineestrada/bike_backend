# Handles request and response cycles of the Web app

from django.shortcuts import render_to_response
from django.template import RequestContext

from django.http import HttpResponse

from django.views import generic
from django.contrib.gis.geos import fromstr
from django.contrib.gis.db.models.functions import Distance
from ..maps/models import Hospital

# Temporarily will have to hardcode a user_location variable with lon and lat
longitude = -80.191788
latitude = 25.761681

user_location = Point(longitude, latitude, srid=4326)

class Home(generic.ListView):
    model = Hospital
    context_object_name = 'hospitals'
    queryset = Hospital.objects.annotate(distance=Distance('location',
    user_location)
    ).order_by('distance')[0:6]
    template_name = 'hospital/index.html'