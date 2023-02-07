from .models import *
from rest_framework import serializers


class TripSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trip
        fields = (
            'start_location',
            'end_location',
            'title',
            'driver',
            'students',
            'riders',
            'review',

        )
    def create(self, validated_data):
        return Trip.objects.create(**validated_data)