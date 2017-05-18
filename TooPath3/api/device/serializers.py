from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer

from TooPath3.api.models import Location, Device


class DeviceLocationSerializer(serializers.Serializer):
    latitude = serializers.FloatField(source='extract_latitude_point', read_only='True')
    longitude = serializers.FloatField(source='extract_longitude_point', read_only='True')

    class Meta:
        model = Device


class LocationSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Location
        geo_field = "location"
        fields = ('did', 'latitude', 'longitude')


class LocationDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('latitude', 'longitude')
