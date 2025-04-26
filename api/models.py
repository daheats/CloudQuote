from django.db import models
from djmoney.models.fields import MoneyField

class Product(models.Model):
    product_name = models.CharField(max_length=255)
    product_price = MoneyField(max_digits=14, decimal_places=2, default_currency="USD")

    def __str__(self):
        return self.product_name


