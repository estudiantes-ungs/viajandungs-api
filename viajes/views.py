from rest_framework import viewsets, generics
from viajes.models import Viaje, Noticia
from .serializers import ViajeSerializer, NoticiaSerializer

class ViajeRUD(viewsets.ModelViewSet):
    queryset = Viaje.objects.all()
    serializer_class = ViajeSerializer

class NoticiaViajeRUD(viewsets.ModelViewSet):
    serializer_class = NoticiaSerializer
    queryset = Noticia.objects.all()
    
    def get_queryset(self):
        queryset = self.queryset
        viaje = self.request.query_params.get('viaje', None)
        if viaje is not None:
            queryset = queryset.filter(viaje = viaje)
        return queryset