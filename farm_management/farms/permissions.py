from rest_framework.permissions import BasePermission
from django.contrib.auth import get_user_model

class IsAdminUser(BasePermission):
    """
    Custom permission to allow only admin users access.
    """

    def has_permission(self, request, view):
        user = request.user
        return user.is_staff  # Check if user is a staff member (admin)
