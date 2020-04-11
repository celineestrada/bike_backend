# Handles request and response cycles of the Web app

from django.views import generic

from django.contrib.gis.db.models.functions import Distance
from django.contrib.gis.geos import Point
from models import Hospital

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
