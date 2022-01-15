
from tkinter import CASCADE
from django.db import models

from category.models import Category
from vendor.models import Vendor

# Create your models here.

class Item(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=11, decimal_places=2)
    image = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name

class Variation(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=11, decimal_places=2,default=0)

    def __str__(self) -> str:
        return self.name

class Topping(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=11, decimal_places=2,default=0)

    def __str__(self) -> str:
        return self.name
