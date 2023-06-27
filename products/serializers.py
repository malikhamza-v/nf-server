from rest_framework import serializers
from .models import Product, ProductImages

class ProductImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImages
        fields = ['id', 'image']

class ProductSerializer(serializers.ModelSerializer):
    images = ProductImagesSerializer(read_only=True, many=True)
    class Meta:
        model = Product
        fields = ['id', 'name','description', 'original_price', 'discounted_price', 'slug', 'available_sizes', 'available_colors', 'category', 'images']
        depth = 1