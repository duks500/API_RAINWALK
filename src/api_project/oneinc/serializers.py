from rest_framework import serializers
from .models import GetInfo

class GetInfo_Modelserializers(serializers.ModelSerializer):
    class Meta:
        model = GetInfo
        fields = '__all__'