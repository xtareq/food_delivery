from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from vendor.models import Vendor
from vendor.serializers import VendorSerializer

# Create your views here.


@csrf_exempt
def vendor_list(request):
    if request.method == "GET":
        vendors = Vendor.objects.all()
        serializer = VendorSerializer(vendors, many=True)
        return JsonResponse(serializer.data, safe=False) 