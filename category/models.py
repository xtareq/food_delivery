
from tkinter import CASCADE
from django.db import models

from vendor.models import Vendor

# Create your models here.

class Category(models.Model):
    vendor = models.ForeignKey(Vendor,on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=200)
    image = models.CharField(max_length=255, default="https://testapi.saxonmarket.com/static/images/defaultCategory.png")

    def __str__(self) -> str:
        return self.name
