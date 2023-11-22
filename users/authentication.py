from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
import jwt
from django.conf import settings
from .models import User

class CustomAuthentication(BaseAuthentication):
    def authenticate(self, request):
        token = request.COOKIES.get('token')

        if not token:
            return None  # No hay token, no se intenta autenticar
        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('El token ha expirado')

        user = User.objects.filter(id=payload['id']).first()
        if user is None:
            raise AuthenticationFailed('Usuario no encontrado')

        return (user, None)