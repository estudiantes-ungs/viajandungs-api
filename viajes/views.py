from rest_framework import viewsets
from viajes.models import Viaje
from .serializers import ViajeSerializer

class ViajeRUD(viewsets.ModelViewSet):
    queryset = Viaje.objects.all()
    serializer_class = ViajeSerializer