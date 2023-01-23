from .models import *
from rest_framework import serializers
from dataclasses import fields

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reviews
        fields = (
            'review',
            'rate',
            'title',
        )
    def create(self, validated_data):
        user = self.context.get('user')
        return Reviews.objects.create(user=user , **validated_data)