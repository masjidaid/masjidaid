from django.db import models
from django.conf import settings


class Campaign(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    target = models.IntegerField()
    # target = models.DecimalField(decimal_places=2, max_digits=8)
    is_active = models.BooleanField(default=False)
