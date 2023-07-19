from rest_framework import serializers
from webPageApp.models import Device
from webPageApp.models import WalkIn


class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = '__all__'  


class WalkInSerializer(serializers.ModelSerializer):
    token = serializers.SerializerMethodField()

    class Meta:
        model = WalkIn
        fields = ('name', 'phone_number', 'email', 'address', 'city', 'country', 'referral_code', 'token')

    def get_token(self, obj):
        # Generate and return the token based on your desired logic
        # Example: Generate a unique token based on the walk-in details
        token = "SOME_TOKEN_GENERATION_LOGIC"
        return token

    def create(self, validated_data):
        token = self.get_token(validated_data)
        walk_in = WalkIn.objects.create(token=token, **validated_data)
        return walk_in