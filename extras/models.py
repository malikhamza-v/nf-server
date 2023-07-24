from django.db import models

class ShippingCost(models.Model):
    shipping_cost = models.DecimalField(decimal_places=2,max_digits=5, default=20.00)

    def __str__(self):
        return f'{self.shipping_cost}'
