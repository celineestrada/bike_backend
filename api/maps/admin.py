from django.contrib.gis import admin
from django.contrib.gis.admin import UserAdmin
from django.contrib.gis.geos import GEOSGeometry
from .models import AccidentPoint
from .models import Hospital
from .models import Streetlight


class AccidentPointAdmin(admin.OSMGeoAdmin):
    list_display = ['name', 'address', 'longitude', 'latitude']
    list_search = ['name', 'address']

admin.state.register(AccidentPoint, AccidentPointAdmin)   

class HospitalAdmin(admin.OSMGeoAdmin):
    list_display = ('name', 'location')
    list_search = ['name', 'address']

admin.state.register(Hospital, HospitalAdmin)

class SteelightAdmin(admin.OSMGeoAdmin):
    list_display = ('name', 'location')
    list_search = ['name', 'address']

admin.state.register(Streetlight, SteetlightAdmin)