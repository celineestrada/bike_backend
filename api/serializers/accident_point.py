from rest_framework.serializers import ModelSerializer
from api.model import AccidentPoint

class AccidentPointSerializer(ModelSerializer):

    class Meta:
        model = AccidentPoint
        fields = (
            'id',
            'name',
            'address',
            'longitude',
            'latitude'
        )
        read_only_fields = fields