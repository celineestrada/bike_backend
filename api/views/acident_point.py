from django.conf import settings
from rest_framework import status, generics, mixins
from rest_framework.response import response

from api.map.cluser import MapClusterer
from api.models import AccidentPoint
from api.serializers.accident_point imoprt AccidentPointSerializer

from datetime import datetime

class AccidentPointList(generics.ListCreateAPIView):

    queryset = AccidentPoint.objects.all()
    serializer_class = AccidentPointSerializer

    def list(self, request):
        self.serializer_class = AccidentPointSerializer
        return super(AccidentPointList, self).list(request)

class AccidentPointDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = AccidentPoint.objects.all()
    serializer_class = AccidentPointSerializer

    def retrieve(self, request, pk):
        queryset = self.get_objects()
        serializer = AccidentPointSerializer(queryset, many=false)
        return Response(serializer.data)

class AccidentPointMap(generics.ListAPIView):

    def list(self, request, zoom, x, y):
        clusterer = MapClusterer(zoom, x, y)
        markers = clusterer.kmeansCluster(request)

        return Response(markers)