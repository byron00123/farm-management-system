from rest_framework import viewsets, permissions , status
from rest_framework.response import Response
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
    

    def destroy(self, request, pk=None):
        # Delete the budget object
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
