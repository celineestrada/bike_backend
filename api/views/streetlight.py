from rest_framework import generics
from rest_framework.response import Response

from maps.models import Streetlight
from serializers.streetlight import StreetlightSerializer


# from api.map.cluster import MapClusterer

class StreetlightList(generics.ListCreateAPIView):
    queryset = Streetlight.objects.all()
    serializer_class = StreetlightSerializer

    def list(self, request):
        self.serializer_class = StreetlightSerializer
        return super(StreetlightList, self).list(request)


class StreetlightDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Streetlight.objects.all()
    serializer_class = StreetlightSerializer

    def retrieve(self, request, pk):
        queryset = self.get_objects()
        serializer = StreetlightSerializer(queryset, many=False)
        return Response(serializer.data)


class StreetlightMap(generics.ListAPIView):

    def list(self, request, zoom, x, y):
        clusterer = MapClusterer(zoom, x, y)
        markers = clusterer.kmeansCluster(request)

        return Response(markers)
