from decimal import Decimal
from django.db import models
from django.conf import settings

# Create your models here.

class Transaction(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    amount = models.IntegerField()
    # amount = models.DecimalField(default=Decimal("0.0"), max_digits=12, decimal_places=2)
    campaign = models.ForeignKey('campaign.Campaign', on_delete=models.CASCADE)
    donor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
