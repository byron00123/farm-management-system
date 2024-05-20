from django.urls import path, include
from rest_framework.routers import DefaultRouter

from farms.views.farm_view import FarmViewSet
from farms.views.budget_view import BudgetViewSet
from farms.views.inventory_item_view import InventoryItemViewSet
from farms.views.inventory_transaction_view import InventoryTransactionViewSet # Assuming named inventory_transaction_view.py
from farms.views.market_price_view import MarketPriceViewSet
from farms.views.task_view import TaskViewSet

router = DefaultRouter()
router.register(r'farms', FarmViewSet)
router.register(r'budgets', BudgetViewSet)
router.register(r'inventory_items', InventoryItemViewSet)
router.register(r'inventory_transactions', InventoryTransactionViewSet)
router.register(r'market_prices', MarketPriceViewSet)
router.register(r'tasks', TaskViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
