from django.contrib import admin
from .models import Farm, Budget, InventoryItem, InventoryTransaction, MarketPrice, Task

admin.site.register(Farm)
admin.site.register(Budget)
admin.site.register(InventoryItem)
admin.site.register(InventoryTransaction)
admin.site.register(MarketPrice)
admin.site.register(Task)
