from django.db import models
from decimal import Decimal


class Accordion(models.Model):
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=50, blank=True, null=True)
    content = models.CharField(max_length=50, blank=True, null=True)
    width = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=Decimal('0.00')
    )
    height = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=Decimal('0.00')
    )
    style = models.TextField(blank=True, null=True)
    sections = models.ManyToManyField(
        'Accordion',
        blank=True,
        on_delete=models.CASCADE
    )
