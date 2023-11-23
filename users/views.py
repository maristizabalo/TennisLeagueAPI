from os import name
from rest_framework.views import APIView
from users.serializers import UserSerializer, JugadorSerializer
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from .models import User
import jwt, datetime

# Create your views here.
class RegisterView(APIView):

    def post(self, request):
        serializer = UserSerializer(data= request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class LoginView(APIView):
    
    def post(self, request):
        username = request.data['username']
        password = request.data['password']

        user = User.objects.filter(username=username).first()
        if user is None:
            return Response({"error": "Usuario no encontrado!"}, status=401)
        
        if not user.check_password(password):
            return Response({"error": "Contraseña incorrecta!"}, status=401)
        
        payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=10),
            'iat': datetime.datetime.utcnow()    
        }

        token = jwt.encode(payload, 'secret', algorithm='HS256')

        response = Response()

        response.set_cookie(key='token', value=token, httponly=True)

        response.data = {
            'token': token,
            'user': {
                "id": user.id,
                "name": user.name,
                "username": user.username,
                "rol": user.rol.id
            }
        }
        
        return response
    
class UserView(APIView):
    def get(self, request):
        token = request.COOKIES.get('token')

        if not token:
            raise AuthenticationFailed('No estas autenticado')
        
        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('No estas autenticado')
        
        user = User.objects.filter(id=payload['id']).first()
        serializer = UserSerializer(user)

        return Response(serializer.data)
    
class LogoutView(APIView):

    def post(self, request):
        response = Response()
        response.delete_cookie('token')
        response.data = {
            "message": "Success"
        }

        return response

class ListaJugadoresView(APIView):
    def get(self, request):
        token = request.COOKIES.get('token')
        if not token:
            raise AuthenticationFailed('No estas autenticado')

        # Se filtran los usuarios con rol de jugador (rol_id=2) el cual es de jugador
        jugadores = User.objects.filter(rol=2)
        serializer = JugadorSerializer(jugadores, many=True)

        return Response(serializer.data)

class DetalleJugadorView(APIView):
    def get(self, request, pk):
        token = request.COOKIES.get('token')
        if not token:
            raise AuthenticationFailed('No estas autenticado')

        try:
            jugador = User.objects.get(id=pk, rol=2)
        except User.DoesNotExist:
            return Response({'error': 'Jugador no encontrado'}, status=404)

        serializer = JugadorSerializer(jugador)
        return Response(serializer.data)
