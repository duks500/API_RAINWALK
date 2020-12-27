from rest_framework import serializers
from .models import GetInfo

class GetInfo_Modelserializers(serializers.ModelSerializer):
    class Meta:
        model = GetInfo
        fields = ['ResponseCode','PortalOneSessionKey','ResponseMessage', 'CustomerId']


    # def create(self, validated_data):
    #     user = GetInfo(
    #         responseCode = validated_data[ResponseCode],
    #         portalOneSessionKey = validated_data[PortalOneSessionKey],
    #         responseMessage = validated_data[ResponseMessage],
    #         customerId = validated_data[CustomerId]
    #     )
    #     user.save()
    #     return user

class CreateUser_Modelserializers(serializers.ModelSerializer):
    class Meta:
        model = GetInfo
        fields = ['PortalOneSessionKey', 'ExternalCustomerId', 'CustomerName']

    # def create(self, validated_data):
    #     user = GetInfo(
    #         externalCustomerId = validated_data[ExternalCustomerId],
    #         PortalOneSessionKey = validated_data[PortalOneSessionKey],
    #         customerName = validated_data[CustomerName]
    #     )
    #     user.save()
    #     return user