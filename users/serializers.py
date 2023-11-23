from rest_framework import serializers
from .models import User, Rol

class RolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rol
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ['id', 'name', 'username', 'password', 'rol']
        extra_kwargs = {
            'password': {'write_only': True}
        }
    
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.rol = Rol.objects.get_or_create(id=2)[0] # Asegúrate que el rol con id=2 exista
        instance.save()
        return instance
