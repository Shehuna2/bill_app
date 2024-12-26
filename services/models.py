from django.db import models
from django.contrib.auth.models import User
from wallet.models import Wallet

class Service(models.Model):
    SERVICE_TYPE = [
        ('airtime', 'Airtime'),
        ('data', 'Data'),
        ('bill', 'Bill Payment'),
    ]
    name = models.CharField(max_length=50)
    service_type = models.CharField(max_length=10, choices=SERVICE_TYPE)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    description = models.TextField(null=True, blank=True)

class Purchase(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='purchases')
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='purchases')
    quantity = models.PositiveIntegerField(default=1)
    total_price = models.DecimalField(max_digits=12, decimal_places=2)
    purchased_at = models.DateTimeField(auto_now_add=True)
