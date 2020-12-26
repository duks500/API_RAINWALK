from rest_framework import serializers
from new.models import GetInfo



class InfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = GetInfo
        fields = ['responseCode' , 'portalOneSessionKey' , 'responseMessage',]







