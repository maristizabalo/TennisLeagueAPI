from rest_framework import generics
from .models import Torneo, Partido
from .serializers import TorneoSerializer, PartidoSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from .models import User
import jwt


# Vistas para Torneo
class ListaTorneos(generics.ListCreateAPIView):
    queryset = Torneo.objects.all()
    serializer_class = TorneoSerializer

class DetalleTorneo(generics.RetrieveUpdateDestroyAPIView):
    queryset = Torneo.objects.all()
    serializer_class = TorneoSerializer

# Vistas para Partido
class ListaPartidos(generics.ListCreateAPIView):
    queryset = Partido.objects.all()
    serializer_class = PartidoSerializer

class DetallePartido(generics.RetrieveUpdateDestroyAPIView):
    queryset = Partido.objects.all()
    serializer_class = PartidoSerializer