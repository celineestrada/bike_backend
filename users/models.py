from django.db import models
from django.contrib.auth.models import User


# Create your models here.
#
# class MapQueries(models.Model):
#     class Meta:
#         app_label = 'bike'
#
#     name = models.CharField(max_length=255, default="Route")
#     origin = models.CharField(max_length=45, null=False)
#     origin_lat = models.FloatField(null=False)
#     origin_lng = models.FloatField(null=False)
#     destination = models.CharField(max_length=45, null=False)
#     destination_lat = models.FloatField(null=False)
#     destination_lng = models.FloatField(null=False)
#     polyline = models.CharField(max_length=510, null=False)
#     score = models.FloatField(null=False)
#     author = models.ForeignKey(User, default=None, on_delete=models.CASCADE)