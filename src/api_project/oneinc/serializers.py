from rest_framework import serializers
from .models import GetInfo

class GetInfo_Modelserializers(serializers.ModelSerializer):
    class Meta:
        model = GetInfo
        fields = '__all__'


    def create(self, validated_data):
        user = GetInfo(
            responseCode = validated_data[ResponseCode],
            portalOneSessionKey = validated_data[PortalOneSessionKey],
            responseMessage = validated_data[ResponseMessage]
        )
        user.save()
        return user