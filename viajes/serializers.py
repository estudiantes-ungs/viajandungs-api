from rest_framework import serializers
from viajes.models import Viaje, Noticia

class ViajeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Viaje
        fields = (
            'pk',
            'name',
            'destination',
            'career',
            'shortDescription',
            'longDescription',
            'eventUrl',
            'departureDate',
            'returnDate',
            'createdAt'
        )

class NoticiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Noticia
        fields = (
            'pk',
            'viaje',
            'name',
            'text',
            'createdAt'
        )