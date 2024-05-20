from rest_framework import viewsets, permissions
from ..models import InventoryItem
from ..serializers import InventoryItemSerializer

class InventoryItemViewSet(viewsets.ModelViewSet):
    queryset = InventoryItem.objects.all()
    serializer_class = InventoryItemSerializer
    permission_classes = [permissions.IsAuthenticated]  # Require authentication for modification

    def get_queryset(self):
        # Filter inventory items based on user or farm (if applicable)
        user = self.request.user
        return InventoryItem.objects.filter(farm__owner__user=user)  # Example filtering by owner
