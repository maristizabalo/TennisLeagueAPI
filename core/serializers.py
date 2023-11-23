from rest_framework import serializers
from .models import Torneo, Partido

class TorneoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Torneo
        fields = ['id', 'nombre', 'ubicacion', 'fecha_inicio', 'fecha_fin', 'jugadores']

class PartidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partido
        fields = ['id', 'torneo', 'jugador1', 'jugador2', 'ganador', 'fecha', 'resultado']