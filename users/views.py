from rest_framework.views import APIView
from users.serializers import UserSerializer
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
            raise AuthenticationFailed('Usuario no encontrado!')
        
        if not user.check_password(password):
            raise AuthenticationFailed('Contraseña incorreta!')
        
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
                'name': user.name,
                'username': user.username,
                'rol': user.rol
            }
        }

        print(response.data)
        
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


