from rest_framework import serializers
from .models import Farm, Budget, InventoryItem, InventoryTransaction, MarketPrice, Task

class FarmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Farm
        fields = '__all__'  # Include all fields (you can customize this)

class BudgetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Budget
        fields = '__all__'  # Include all fields (you can customize this)

class InventoryItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = InventoryItem
        fields = '__all__'  # Include all fields (you can customize this)

class InventoryTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = InventoryTransaction
        fields = '__all__'  # Include all fields (you can customize this)

class MarketPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = MarketPrice
        fields = '__all__'  # Include all fields (you can customize this)

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'  # Include all fields (you can customize this)
