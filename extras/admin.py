from django.contrib import admin
from .models import ShippingCost

class ShippingCostAdmin(admin.ModelAdmin):
    def has_add_permission(self, request): # Here
        return not ShippingCost.objects.exists()

admin.site.register(ShippingCost, ShippingCostAdmin)
