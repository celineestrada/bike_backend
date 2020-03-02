from django.contrib.gis.admin import OSMGeoAdmin
from .models import Hospital

@admin.register(Hospital)
class HospitalAdmin(OSMGeoAdmin):
    list_display = ('name', 'location')

@admin.register(StreetLights)
class SteetLightAdmin(OSMGeoAdmin):
    list_display = ('name', 'location')