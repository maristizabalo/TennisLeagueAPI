# Proyecto Tenis League BACKEND PYTHON REST API

# Instalación ambiente

## Requisitos
- Linux, PostgreSQL y Python 3.8+

## Instalación
1. Instalar las dependencias necesarias del proyecto:

```
sudo apt-get install gcc libpq-dev python-dev python3-dev python3-venv build-essential libmagic nodejs
```
Nota: El servicio de Memcached es necesario para el proyecto, puede instalarse usando la siguiente guía: https://www.digitalocean.com/community/tutorials/how-to-install-and-secure-memcached-on-ubuntu-20-04

- Para iniciar rápidamente el servicio de Memcached correr:
```
sudo apt install memcached
sudo systemctl start memcached
```

2. Descargar el proyecto del repositorio
```
git clone https://github.com/maristizabalo/TennisLeagueAPI.git
```

3. Crear ambiente virtual de python y activarlo
```
cd TennisLeagueAPI
python3 -m venv venv
source venv/bin/activate para Linux/Mac o para Windows venv/Scripts/activate
```

4. Instalar dependencias de python del proyecto
```
pip install -r requirements.txt 
```


5. Modificar el archivo de configuraciones del proyecto en "project/settings/production.py". Todos los valores que tengan un "?" al final pueden ser modificados.

6. Crear y llenar base de datos:
```
# crear migraciones en la base de datos
python manage.py migrate
# para alimentar la base de datos con valores precargados en "fixtures/":
python manage.py loaddata fixtures/*
```

- Nota: Para reiniciar la base de datos en desarrollo (en Linux) correr el script llamado "reser_db.sh"

7. Para correr la aplicacion en produccion (usando server de Django) correr:
```
python manage.py runserver --settings=project.settings.production
```
- Nota: Para usar el motor de base de datos Postgresql, descomentar las líneas 3 y 4 del archivo "requirements.txt" y volver a instalar las dependencias.