
from rest_framework import serializers
from item.serializers import ItemSerializer

from vendor.models import Vendor


class VendorSerializer(serializers.ModelSerializer):
    items = serializers.StringRelatedField(many=True)
    class Meta:
        model = Vendor
        fields = ['id', 'name', 'phone','items']
