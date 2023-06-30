from rest_framework.decorators import api_view


# @api_view(['POST'])
# def place_order(request, *args, **kwargs):
#     slug = kwargs['slug']
    
#     qs = Product.objects.filter(slug=slug)
#     if qs:
#         serializer = ProductSerializer(qs, many=True)
#         return Response({'data': serializer.data})
#     else:
#         return Response({'error':404})  
