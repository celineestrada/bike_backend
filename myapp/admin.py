from django.contrib.gis import admin
from django.contrib.gis.admin import UserAdmin
from django.contrib.gis.geos import GEOSGeometry
from .models import Hospital

class AccidentPointAdmin(admin.OSMGeoAdmin):
    list_display = ['name', 'address', 'longitude', 'latitude']
    list_search = ['name', 'address']

admin.state.register(AccidentPoint, AccidentPointAdmin)   

class HospitalAdmin(OSMGeoAdmin):
    list_display = ('name', 'location')
    list_search = ['name', 'address']

admin.state.register(Hospital, HospitalAdmin)

class SteetLightAdmin(OSMGeoAdmin):
    list_display = ('name', 'location')
    list_search = ['name', 'address']

admin.state.register(StreetLight, SteetLightAdmin)