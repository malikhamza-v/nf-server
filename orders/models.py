from django.db import models
from useraccounts.models import CustomUserModel
class Orders(models.Model):
    user = models.ForeignKey(CustomUserModel, on_delete=models.CASCADE, related_name='orders')
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email_address = models.CharField(max_length=150)
    phone_no = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    zip_code = models.IntegerField()
    address = models.TextField(max_length=500)
