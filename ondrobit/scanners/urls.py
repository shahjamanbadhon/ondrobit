from django.urls import path
from . import views

urlpatterns = [
    path('scan/', views.scan_page, name='scan_page'),
    path('physical-scanner/', views.physical_scanner, name='physical_scanner'),
]
