from django.urls import path
from .views import GetProducts

urlpatterns = [
    path('api/get-all-products/', GetProducts.as_view(), name='get_all_products')
]

