from rest_framework.decorators import api_view
from .models import Product
from rest_framework.response import Response
from .serializers import ProductSerializer
from rest_framework import generics


class GetProducts(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


@api_view(['GET'])
def get_single_product(request, *args, **kwargs):
    slug = kwargs['slug']
    qs = Product.objects.filter(slug=slug)
    serializer = ProductSerializer(qs, many=True)
    return Response({'data': serializer.data})
