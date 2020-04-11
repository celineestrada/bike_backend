from django.contrib.gis import admin

from . import models


class AccidentPointAdmin(admin.OSMGeoAdmin):
    list_display = ['id', 'latitude', 'longitude']
    list_search = ['id', 'latitude', 'longitude']


admin.site.register(models.AccidentPoint, AccidentPointAdmin)


class HospitalAdmin(admin.OSMGeoAdmin):
    list_display = ('id', 'name', 'latitude', 'longitude')
    list_search = ['id', 'name']


admin.site.register(models.Hospital, HospitalAdmin)


class SteetlightAdmin(admin.OSMGeoAdmin):
    list_display = ('id', 'latitude', 'longitude')
    list_search = ['id', 'latitude', 'longitude']


admin.site.register(models.Streetlight, SteetlightAdmin)
