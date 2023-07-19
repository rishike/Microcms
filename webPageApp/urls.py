from django.urls import path
from webPageApp.views import device_list
from webPageApp.views import lead_capture
from webPageApp.api.views import DeviceListAPIView
from webPageApp.api.views import WalkInCreateAPIView

urlpatterns = [
    # Other URL patterns
    path('', device_list, name='device_list'),
    path('lead-capture/', lead_capture, name='lead_capture'),
    path('api/devices/', DeviceListAPIView.as_view(), name='device-list'),
    path('api/walk-in/', WalkInCreateAPIView.as_view(), name='walk-in-create'),
]