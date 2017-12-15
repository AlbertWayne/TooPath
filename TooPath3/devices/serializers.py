from rest_framework import serializers

from TooPath3.constants import DEFAULT_ERROR_MESSAGES
from TooPath3.models import Device
from TooPath3.tracks.serializers import TrackSerializer


class DeviceSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    tracks = TrackSerializer(many=True, read_only=True)

    class Meta:
        model = Device
        fields = '__all__'

    def validate(self, data):
        if self.partial is True:
            if 'pk' in data or 'did' or 'device_type' or 'device_privacy' or 'trash' in data:
                raise serializers.ValidationError(DEFAULT_ERROR_MESSAGES['invalid_patch'])
            if bool(data) is False or len(self.initial_data) != len(data):
                raise serializers.ValidationError(DEFAULT_ERROR_MESSAGES['patch_device_fields_required'])
        return data
