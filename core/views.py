from rest_framework import generics
from .models import Jugador, Torneo, Partido
from .serializers import JugadorSerializer, TorneoSerializer, PartidoSerializer

# Vistas para Jugador
class ListaJugadores(generics.ListCreateAPIView):
    queryset = Jugador.objects.all()
    serializer_class = JugadorSerializer

class DetalleJugador(generics.RetrieveUpdateDestroyAPIView):
    queryset = Jugador.objects.all()
    serializer_class = JugadorSerializer

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