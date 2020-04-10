from django.contrib.gis import admin

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


class SteetlightAdmin(admin.OSMGeoAdmin):
    list_display = ('name', 'location')
    list_search = ['name', 'address']


admin.state.register(Streetlight, SteetlightAdmin)
