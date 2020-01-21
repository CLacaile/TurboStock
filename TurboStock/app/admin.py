from django.contrib import admin
from app.models import CEO, StoreManager, Store, AisleManager, Aisle, Product, Stock

admin.site.register(CEO)
admin.site.register(StoreManager)
admin.site.register(Store)
admin.site.register(AisleManager)
admin.site.register(Aisle)
admin.site.register(Product)
admin.site.register(Stock)

