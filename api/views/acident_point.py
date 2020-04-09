from rest_framework import generics
from rest_framework.response import Response

from maps.models import AccidentPoint
from serializers.accident_point import AccidentPointSerializer

# from api.map.cluser import MapClusterer


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
        serializer = AccidentPointSerializer(queryset, many=False)
        return Response(serializer.data)


class AccidentPointMap(generics.ListAPIView):

    def list(self, request, zoom, x, y):
        clusterer = MapClusterer(zoom, x, y)
        markers = clusterer.kmeansCluster(request)

        return Response(markers)
