from django.urls import path
from .views import getShippingCost

urlpatterns = [
    path('get-shipping-cost/', getShippingCost.as_view()),
] 

