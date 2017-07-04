from rest_framework import serializers
from rest_framework_gis import serializers as gis_serializers

from TooPath3.devices.constants import DEFAULT_ERROR_MESSAGES
from TooPath3.models import ActualLocation


class CoordinatesSerializer(serializers.Serializer):
    latitude = serializers.FloatField()
    longitude = serializers.FloatField()


class ActualLocationSerializer(gis_serializers.GeoFeatureModelSerializer):
    class Meta:
        model = ActualLocation
        geo_field = 'point'
        fields = '__all__'

    def validate(self, data):
        if (data['point'].x < -90.0) or (data['point'].x > 90.0):
            raise serializers.ValidationError(DEFAULT_ERROR_MESSAGES['invalid_latitude'])
        if (data['point'].y < -180) or (data['point'].y > 180):
            raise serializers.ValidationError(DEFAULT_ERROR_MESSAGES['invalid_longitude'])
        return data