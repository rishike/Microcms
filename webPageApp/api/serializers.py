from rest_framework import serializers
from webPageApp.models import Device
from webPageApp.models import WalkIn


class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = '__all__'  


class WalkInSerializer(serializers.ModelSerializer):
    # token_number = serializers.SerializerMethodField()

    class Meta:
        model = WalkIn
        fields = ('lead', 'vendor', 'device', 'currency', 'offer_price', 'walkin_datetime', 'token_number')
        read_only_fields = ('token_number',)

    # def get_token_number(self, obj):

    #     token = WalkIn.objects.all().last().token_number
    #     token = token+1
    #     return token

    def create(self, validated_data):
        token = WalkIn.objects.all().last().token_number + 1
        walk_in = WalkIn.objects.create(token_number=token, **validated_data)
        return walk_in