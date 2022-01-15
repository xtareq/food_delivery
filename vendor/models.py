from django.db import models

# Create your models here.

class Vendor(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=199, unique = True)
    phone = models.CharField(max_length=255, unique=True,null=True)
    logo = models.CharField(max_length=255, default="https://testapi.saxonmarket.com/static/images/defaultUser.png")
    address = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name+" ("+self.address+")"