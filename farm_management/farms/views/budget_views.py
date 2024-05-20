from rest_framework import viewsets, permissions
from ..models import Budget
from ..serializers import BudgetSerializer

class BudgetViewSet(viewsets.ModelViewSet):
    queryset = Budget.objects.all()
    serializer_class = BudgetSerializer
    permission_classes = [permissions.IsAuthenticated]  # Require authentication for modification

    def get_queryset(self):
        # Filter budgets based on user or farm (if applicable)
        user = self.request.user
        return Budget.objects.filter(farm__owner__user=user)  # Example filtering by owner
