from rest_framework import serializers
from .models import Orders

class CreateOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = ('id', 'user', 'first_name', 'last_name', 'email_address', 'phone_no', 'country', 'state', 'city', 'zip_code', 'address_one', 'address_two', 'order_description', 'is_card_payment', 'order_total')

class GetOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = ('id', 'user', 'created_at', 'status', 'order_total' )