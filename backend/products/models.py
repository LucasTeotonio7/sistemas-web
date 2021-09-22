from suppliers.models import Supplier
from django.db import models

# Create your models here.


class Product(models.Model):
    MEASURE_CHOICES = (
        ("KG", "Kilograma"),
        ("G", "Grama"),
        ("L", "Litro"),
        ("ML", "Mililitro")
    )

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=False, blank=False)
    unit_measurement = models.CharField(max_length=2, choices=MEASURE_CHOICES, null=False, blank=False)
    registration_date = models.DateField(null=False, blank=False)
    purchase_price = models.FloatField(max_length=6,null=False, blank=False)


class Purchase(models.Model):
    id = models.AutoField(primary_key=True)
    purchase_date = models.DateField(null=False, blank=False)
    quantity = models.FloatField(max_length=6,null=False, blank=False)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    supplier = models.ForeignKey(Supplier, on_delete=models.PROTECT)


class individualPurchasePrice(models.Model):
    id = models.AutoField(primary_key=True)
    purchase_price = models.FloatField(max_length=6,null=False, blank=False)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    supplier = models.ForeignKey(Supplier, on_delete=models.PROTECT)