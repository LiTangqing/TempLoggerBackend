from rest_framework import serializers
from rest_framework_mongoengine import serializers as mongoserializers

from models import Trip


class TripSerializer(mongoserializers.DocumentSerializer):
    class Meta:
        model = Trip
        fields = '__all__'
        depth = 2
