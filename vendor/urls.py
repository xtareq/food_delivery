from django.urls import path
from vendor import views

urlpatterns = [
    path('vendors/', views.vendor_list)
]