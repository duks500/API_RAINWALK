from rest_framework import serializers
from .models import Article


### This is an example class of how to use serializers.Serializer. ###
class ArticleSerializer_serializers(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    author = serializers.CharField(max_length=100)
    email = serializers.EmailField(max_length=100)
    date = serializers.DateTimeField()

    ## A create method ##
    def create(self, validated_data):
        return Article.objects.create(validated_data)

    ## An update method ##
    def update(self,instance,validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.author = validated_data.get('author', instance.author)
        instance.email = validated_data.get('email', instance.email)
        instance.date = validated_data.get('date', instance.date)
        instance.save()
        return instance


### This is an example class of how to use serializers.ModelSerializer ####
class ArticleSerializer_Modelserializers(serializers.ModelSerializer):
    class Meta: #just like a ModelForm class
        model = Article #specify the model name
        # fields = ['id','title','author'] #specify the fields
        fields = '__all__' #get all fields
