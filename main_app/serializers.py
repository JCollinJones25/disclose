from rest_framework import serializers
from .models import Location


class LocationSerializer(serializers.Serializer):
    
    class Meta:
        model = Location
        fields = ['name', 'city', 'state', 'img', 'description']
