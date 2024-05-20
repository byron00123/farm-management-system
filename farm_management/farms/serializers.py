from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import Farm, Budget, InventoryItem, InventoryTransaction, MarketPrice, Task

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email']  # You can add more user fields as needed

class UpdateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email']

class PasswordSerializer(serializers.Serializer):
    current_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

    def validate(self, data):
        user = self.context['request'].user
        if not user.check_password(data['current_password']):
            raise serializers.ValidationError({'current_password': 'Wrong password'})
        return data

class FarmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Farm
        # Customize fields to include what you need
        fields = ['id', 'name', 'location', 'owner']  # Example

class BudgetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Budget
        # Customize fields to include what you need
        fields = ['id', 'farm', 'year', 'amount']  # Example

class InventoryItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = InventoryItem
        # Customize fields to include what you need
        fields = ['id', 'name', 'description', 'category', 'quantity']  # Example

class InventoryTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = InventoryTransaction
        # Customize fields to include what you need
        fields = ['id', 'item', 'quantity', 'type', 'date']  # Example

class MarketPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = MarketPrice
        # Customize fields to include what you need
        fields = ['id', 'item', 'price', 'date', 'location']  # Example

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        # Customize fields to include what you need
        fields = ['id', 'name', 'description', 'farm', 'deadline', 'status']  # Example
