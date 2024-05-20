from rest_framework import viewsets, permissions
from rest_framework.response import Response
from ..models import Farm
from ..serializers import FarmSerializer

class FarmViewSet(viewsets.ModelViewSet):
    queryset = Farm.objects.all()
    serializer_class = FarmSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def retrieve(self, request, pk=None):
        farm = self.get_object()
        # Optional: Include additional details like associated budgets, inventory items, etc.
        return Response(self.serializer_class(farm).data)
