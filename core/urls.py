from django.urls import path
from . import views

urlpatterns = [
    path('torneos/', views.ListaTorneos.as_view(), name='lista-torneos'),
    path('torneos/<int:pk>/', views.DetalleTorneo.as_view(), name='detalle-torneo'),
    path('partidos/', views.ListaPartidos.as_view(), name='lista-partidos'),
    path('partidos/<int:pk>/', views.DetallePartido.as_view(), name='detalle-partido'),
]