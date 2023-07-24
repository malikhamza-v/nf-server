from django.db import models
from useraccounts.models import CustomUserModel

class Orders(models.Model):

    order_status = [
        ('1', "In Progress"),
        ('2', "Shipped"),
    ]
      
    user = models.ForeignKey(CustomUserModel, on_delete=models.SET_NULL, null=True)
    first_name = models.CharField(max_length=150, null=True)
    last_name = models.CharField(max_length=150, null=True)
    email_address = models.CharField(max_length=150, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    phone_no = models.CharField(max_length=255, null=True)
    country = models.CharField(max_length=50, null=True)
    state = models.CharField(max_length=50, null=True)
    city = models.CharField(max_length=50, null=True)
    zip_code = models.CharField(max_length=50, null=True)
    address_one = models.TextField(max_length=500, null=True)
    address_two = models.TextField(max_length=500, null=True, blank=True)
    order_description = models.TextField(max_length=500,  null=True)
    is_card_payment = models.BooleanField(default=True)
    order_total = models.DecimalField(max_digits=7, decimal_places=2, null=True)
    status = models.CharField(max_length=10, choices=order_status, default='1')
    
    def __str__(self):
        return f'{self.user}'

