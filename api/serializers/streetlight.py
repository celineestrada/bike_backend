from rest_framework.serializers import ModelSerializer
from models import Streetlight


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
