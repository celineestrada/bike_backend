from rest_framework.serializers import ModelSerializer
from api.model import Streetlight

class StreetlightSerializer(ModelSerializer):

    class Meta:
        model = Streetlight
        fields = (
            'id',
            'address',
            'longitude',
            'latitude'
        )
        read_only_fields = fields