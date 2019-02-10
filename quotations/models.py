from django.db import models

# Create your models here.


class Quotations(models.Model):

    created_on = models.DateTimeField(default=timezone.now, blank=True)
    currency = models.CharField(max_length=3)
    buy = models.DecimalField(decimal_places=3)
    sell = models.DecimalField(decimal_places=3)
    variation = models.DecimalField(decimal_places=3)
