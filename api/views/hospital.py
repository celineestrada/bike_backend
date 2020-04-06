from django.conf import settings
from rest_framework import status, generics, mixins
from rest_framework.response import Response

from api.map.cluster import MapClusterer
from api.models import Hospital
from api.serializers.hospital import HospitalSerializer

from datetime import datetime

class HospitalList(generics.ListCreateAPIView):

    queryset = Hospital.objects.all()
    serializer_class = HospitalSerializer

    def list(self, request):
        self.serializer_class = HospitalSerializer
        return super(HospitalList, self).list(request)

class HospitalDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Hospital.objects.all()
    serializer_class = HospitalSerializer

    def retrieve(self, request, pk):
        queryset = self.get_objects()
        serializer = HospitalSerializer(queryset, many=false)
        return Response(serializer.data)

class HospitalMap(generics.ListAPIView):

    def list(self, request, zoom, x, y):
        clusterer = MapClusterer(zoom, x, y)
        markers = clusterer.kmeansCluster(request)

        return Response(markers)