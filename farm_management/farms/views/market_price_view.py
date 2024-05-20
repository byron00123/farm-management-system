from rest_framework import viewsets, permissions
from ..models import MarketPrice
from ..serializers import MarketPriceSerializer

class MarketPriceViewSet(viewsets.ModelViewSet):
    queryset = MarketPrice.objects.all()
    serializer_class = MarketPriceSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]  # Allow read-only access
