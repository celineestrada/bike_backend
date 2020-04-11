from rest_framework.serializers import ModelSerializer
from models import Hospital


class HospitalSerializer(ModelSerializer):
    class Meta:
        model = Hospital
        fields = (
            'id',
            'name',
            'address',
            'longitude',
            'latitude'
        )
        read_only_fields = fields
