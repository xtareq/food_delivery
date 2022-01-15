from django.contrib import admin
from vendor.models import Vendor
from django.utils.html import format_html
# Register your models here.

class VendorAdmin(admin.ModelAdmin):
    def logo(self, obj):
        return format_html('<img src="{logo}" />'.format(obj.image.url))
    logo.short_description = "Image"
    list_display = ['name','email','phone','address',"logo"]
admin.site.register(Vendor, VendorAdmin)
