from rest_framework import viewsets
from .models import Distancia
from .serializer import DistanciaSerializer

class DistanciaViewSet(viewsets.ModelViewSet):
    queryset = Distancia.objects.all().order_by('-created')
    serializer_class = DistanciaSerializer