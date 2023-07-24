from rest_framework import serializers
from .models import ShippingCost

class ShippingCostSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShippingCost
        fields = ('shipping_cost', )