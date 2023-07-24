from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny
from .serializers import ShippingCostSerializer
from .models import ShippingCost

class getShippingCost(ListAPIView):
    permission_classes = (AllowAny, )
    serializer_class = ShippingCostSerializer

    def get_queryset(self):
        queryset = ShippingCost.objects.all()
        return queryset[:1]
