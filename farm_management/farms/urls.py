from django.urls import path, include
from rest_framework.routers import DefaultRouter

from farms.views.farm_view import FarmViewSet
from farms.views.budget_view import BudgetViewSet
from farms.views.inventory_item_view import InventoryItemViewSet
from farms.views.inventory_transaction_view import InventoryTransactionViewSet  # Assuming named inventory_transaction_view.py
from farms.views.market_price_view import MarketPriceViewSet
from farms.views.task_view import TaskViewSet
from farms.views.user_view import RegisterView, LoginView, UserLogoutView, UserRetrieveView, ProfileUpdateView, PasswordUpdateView, UserDeleteView

router = DefaultRouter()
router.register(r'farms', FarmViewSet)
router.register(r'budgets', BudgetViewSet)
router.register(r'inventory_items', InventoryItemViewSet)
router.register(r'inventory_transactions', InventoryTransactionViewSet)
router.register(r'market_prices', MarketPriceViewSet)
router.register(r'tasks', TaskViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('users/me/', UserRetrieveView.as_view(), name='user-retrieve'),
    path('users/me/', ProfileUpdateView.as_view(), name='profile-update'),
    path('users/me/password/', PasswordUpdateView.as_view(), name='password-update'),
    path('users/me/', UserDeleteView.as_view(), name='user-delete'),
]
