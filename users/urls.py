from django.urls import path
from .views import LogoutView, RegisterView, LoginView, UserView, ListaJugadoresView, DetalleJugadorView

urlpatterns = [
    path('register', RegisterView.as_view()),
    path('login', LoginView.as_view()),
    path('user', UserView.as_view()),
    path('logout', LogoutView.as_view()),
    path('jugadores/', ListaJugadoresView.as_view(), name='lista-jugadores'),
    path('jugadores/<int:pk>/', DetalleJugadorView.as_view(), name='detalle-jugador'),
]
