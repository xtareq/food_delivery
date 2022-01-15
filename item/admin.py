from django.contrib import admin
from item.models import Item, Topping, Variation 
# Register your models here.
admin.site.register(Item)
admin.site.register(Topping)
admin.site.register(Variation)