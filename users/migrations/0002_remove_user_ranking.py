# Generated by Django 4.2.7 on 2023-11-20 08:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='ranking',
        ),
    ]
