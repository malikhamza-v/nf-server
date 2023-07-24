from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework.views import APIView
from .models import Orders
from .serializers import CreateOrderSerializer, GetOrderSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


class CreateOrder(CreateAPIView):
    # permission_classes = (IsAuthenticated, )
    queryset = Orders.objects.all()
    serializer_class = CreateOrderSerializer

class getUserOrders(APIView):

    def get(self, request, **kwargs):
        user_id = request.GET.get('user_id')
        print('=user_id', user_id)
        query = Orders.objects.filter(user = user_id)
        if query.exists():
            serializer = GetOrderSerializer(query, many=True)
            return Response(serializer.data)
            
        return Response('Server Error!')