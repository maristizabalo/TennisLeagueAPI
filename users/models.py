from django.db import models
from django.contrib.auth.models import AbstractUser

class Rol(models.Model):
    id = models.BigAutoField(primary_key=True, db_column='ID_ROL')
    nombre = models.CharField(unique=True, max_length=100, db_column='NOMBRE')
    descripcion = models.TextField(max_length=2000, db_column='DESCRIPCION')
    activo = models.BooleanField(default=True, db_column='ACTIVO')

    class Meta:
        db_table = 'ROL'
        verbose_name = "ROL"
        verbose_name_plural = "ROLES"

    def __str__(self) -> str:
        return f'id: {self.id} - {self.nombre}'
    
class User(AbstractUser):
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    rol = models.ForeignKey(Rol, on_delete=models.SET_NULL, null=True, blank=True, related_name='usuarios', default=2)
    ranking = models.IntegerField(null=True, blank=True)
    estadisticas = models.CharField(max_length=255, null=True, blank=True) 

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []






    