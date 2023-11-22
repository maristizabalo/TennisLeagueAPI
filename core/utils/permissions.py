from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsAdminOrReadOnly(BasePermission):
    """
    Permiso personalizado que permite solo a los administradores editar la información.
    Los demás usuarios solo pueden leer.
    """

    def has_permission(self, request, view):
        # Comprueba si el método es seguro (GET, HEAD o OPTIONS)
        if request.method in SAFE_METHODS:
            return True

        # Comprueba si el usuario es administrador
        return request.user and request.user.is_staff

class IsAdminUser(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.rol == 'Jugador'