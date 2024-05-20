from rest_framework import viewsets, permissions
from ..models import Task
from ..serializers import TaskSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]  # Require authentication for modification

    def get_queryset(self):
        # Filter tasks based on user or farm (if applicable)
        user = self.request.user
        return Task.objects.filter(farm__owner__user=user)  # Example filtering by owner
