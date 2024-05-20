from rest_framework import viewsets, permissions
from ..models import InventoryTransaction
from ..serializers import InventoryTransactionSerializer

class InventoryTransactionViewSet(viewsets.ModelViewSet):
    queryset = InventoryTransaction.objects.all()
    serializer_class = InventoryTransactionSerializer
    permission_classes = [permissions.IsAuthenticated]  # Require authentication for modification
