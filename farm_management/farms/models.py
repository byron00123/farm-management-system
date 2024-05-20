from django.db import models
from django.contrib.auth.models import User  # Import User model for authentication

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)  # Link to User model
    phone_number = models.CharField(max_length=20, blank=True)
    address = models.CharField(max_length=255, blank=True)
    # Add other user profile specific fields

class Farm(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255, blank=True)
    owner = models.ForeignKey(UserProfile, on_delete=models.CASCADE)  # Link to user profile (farm owner)
    size = models.FloatField(blank=True, null=True)  # Example: area in hectares
    # Add other relevant farm details

class Budget(models.Model):
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE)  # Link to farm
    category = models.CharField(max_length=255)  # Budget category (e.g., seeds, fertilizer)
    amount = models.DecimalField(max_digits=10, decimal_places=2)  # Budget amount
    start_date = models.DateField(blank=True, null=True)  # Optional: Budget start date
    end_date = models.DateField(blank=True, null=True)  # Optional: Budget end date

class InventoryItem(models.Model):
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE)  # Link to farm
    name = models.CharField(max_length=255)
    quantity = models.IntegerField()  # Quantity in stock
    unit = models.CharField(max_length=255, blank=True)  # Unit of measurement (e.g., kg, liters)
    description = models.TextField(blank=True)  # Optional: Description

class InventoryTransaction(models.Model):
    inventory_item = models.ForeignKey(InventoryItem, on_delete=models.CASCADE)  # Link to inventory item
    type = models.CharField(max_length=255)  # Transaction type (e.g., purchase, sale, use)
    quantity = models.IntegerField()  # Positive for addition, negative for removal
    date = models.DateField(auto_now_add=True)  # Automatically record transaction date
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)  # Optional: Price per unit

class MarketPrice(models.Model):
    product = models.CharField(max_length=255)  # Product name (e.g., corn, milk)
    unit = models.CharField(max_length=255, blank=True)  # Unit of measurement (optional)
    price = models.DecimalField(max_digits=10, decimal_places=2)

# New model for Task Scheduling
class Task(models.Model):
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE)  # Link to farm
    name = models.CharField(max_length=255)  # Task name
    description = models.TextField(blank=True)  # Optional: Task description
    start_date = models.DateField()  # Task start date
    due_date = models.DateField()  # Task due date
    priority = models.CharField(max_length=255, choices=[  # Optional: Priority level
        ('HIGH', 'High'),
        ('MEDIUM', 'Medium'),
        ('LOW', 'Low'),
    ], blank=True, null=True)
    completed = models.BooleanField(default=False)  # Track task completion status
