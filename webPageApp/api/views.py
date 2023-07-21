from rest_framework import generics
from webPageApp.models import Device
from webPageApp.api.serializers import DeviceSerializer

from webPageApp.models import WalkIn
from webPageApp.api.serializers import WalkInSerializer

class AvailableDevicesAPIView(generics.ListAPIView):
    queryset = Device.objects.filter(status=True)  # Filter available devices based on the 'status' field
    serializer_class = DeviceSerializer


class WalkInCreateAPIView(generics.CreateAPIView):
    queryset = WalkIn.objects.all()
    serializer_class = WalkInSerializer