from django.urls import path
from .views import CreateOrder, getUserOrders

urlpatterns = [
    path('create-order/', CreateOrder.as_view()),
    path('get-user-orders/', getUserOrders.as_view())
] 



