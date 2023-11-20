from django.db import models
from users.models import User

class Jugador(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    ranking = models.IntegerField()
    estadisticas = models.TextField()

class Torneo(models.Model):
    nombre = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=100)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    jugadores = models.ManyToManyField(Jugador, through='Inscripcion')

class Inscripcion(models.Model):
    jugador = models.ForeignKey(Jugador, on_delete=models.CASCADE)
    torneo = models.ForeignKey(Torneo, on_delete=models.CASCADE)
    fecha_inscripcion = models.DateField(auto_now_add=True)

class Partido(models.Model):
    torneo = models.ForeignKey(Torneo, on_delete=models.CASCADE)
    jugador1 = models.ForeignKey(Jugador, related_name='partidos_jugador1', on_delete=models.CASCADE)
    jugador2 = models.ForeignKey(Jugador, related_name='partidos_jugador2', on_delete=models.CASCADE)
    ganador = models.ForeignKey(Jugador, related_name='partidos_ganados', on_delete=models.CASCADE, null=True, blank=True)
    fecha = models.DateField()
    resultado = models.CharField(max_length=100, blank=True)