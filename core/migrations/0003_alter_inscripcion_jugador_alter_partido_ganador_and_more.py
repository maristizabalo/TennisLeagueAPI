# Generated by Django 4.2.7 on 2023-11-23 04:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0002_alter_jugador_ranking'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inscripcion',
            name='jugador',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='partido',
            name='ganador',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='partidos_ganados', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='partido',
            name='jugador1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='partidos_jugador1', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='partido',
            name='jugador2',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='partidos_jugador2', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='torneo',
            name='jugadores',
            field=models.ManyToManyField(through='core.Inscripcion', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Jugador',
        ),
    ]
