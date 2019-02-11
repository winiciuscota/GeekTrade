from django.db import models
from django.utils import timezone


# Create your models here.


class Quotation(models.Model):

    created_on = models.DateTimeField(default=timezone.now, blank=True)
    currency = models.CharField(max_length=3)
    buy = models.DecimalField(max_digits=10, decimal_places=3, null=True)
    sell = models.DecimalField(max_digits=10, decimal_places=3, null=True)
    variation = models.DecimalField(max_digits=10, decimal_places=3)
