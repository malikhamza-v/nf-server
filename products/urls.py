from django.urls import path
from .views import GetProducts, get_single_product

urlpatterns = [
    path('get-all-products/', GetProducts.as_view(), name='get_all_products'),
    path('get-product/<str:slug>', get_single_product)
]



