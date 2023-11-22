from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from .models import Jugador, Torneo, Inscripcion, Partido
from .serializers import JugadorSerializer, TorneoSerializer, InscripcionSerializer, PartidoSerializer

class JugadorListCreate(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        jugadores = Jugador.objects.all()
        serializer = JugadorSerializer(jugadores, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = JugadorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class TournamentsView(APIView):

    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]
        if self.request.method == 'POST':
            return [IsAuthenticated()]
        return [IsAuthenticated()]

    def get(self, request):
        print(request)
        jugadores = Torneo.objects.all()
        serializer = TorneoSerializer(jugadores, many=True)
        return Response(serializer.data)

    def post(self, request):
        print("Si pasa algo?")
        serializer = TorneoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)