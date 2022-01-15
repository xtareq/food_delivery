from django.db import models

# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=199, unique = True)
    phone = models.CharField(max_length=255, unique=True,null=True)
    avatar = models.CharField(max_length=255, default="https://testapi.saxonmarket.com/static/images/defaultUser.png")
    password = models.CharField(max_length=255)
    verifiedAt= models.DateTimeField("verified at")
    blocked = models.BooleanField(max_length=1,default=False)

    def __str__(self) -> str:
        return self.name
