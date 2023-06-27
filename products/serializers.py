from rest_framework import serializers
from .models import Product, ProductImages

class ProductImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImages
        fields = ['id', 'image', 'is_thumbnail']

class ProductSerializer(serializers.ModelSerializer):
    images = ProductImagesSerializer(read_only=True, many=True)
    class Meta:
        model = Product
        fields = ['id', 'name','short_description','long_description', 'original_price','is_at_discount', 'discounted_percent', 'slug', 'available_sizes', 'available_colors', 'category', 'images']
        depth = 1