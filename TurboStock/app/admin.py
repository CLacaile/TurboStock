from django.contrib import admin
from .models import CEO, StoreManager, Store, AisleManager, Aisle, Product, Stock

admin.register(CEO)
admin.register(StoreManager)
admin.register(Store)
admin.register(AisleManager)
admin.register(Aisle)
admin.register(Product)
admin.register(Stock)
