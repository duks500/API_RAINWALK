from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import GetInfo
from .serializers import GetInfo_Modelserializers

from rest_framework import status, generics, mixins, viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status, generics, mixins, viewsets

import requests
# Create your views here.

class GetInfoID(viewsets.GenericViewSet, mixins.RetrieveModelMixin):
    serializer_class = GetInfo_Modelserializers ##serilaze the data
    queryset = GetInfo.objects.all() #add all the datas to a query set

    lookup_field = 'id' #instead of using pk, I am using an id

    ## A get method ##
    def get(self, request, id=None):

        if id:
            return self.retrieve(request)

        else:
            t = requests.get('https://stgportalone.processonepayments.com/Api/Api/Session/Create')
            ts = t.json()
            return self.list(request)


    ## A post method ##
    def post(self, request):
        return self.create(request) #return the created object


    ## A put method ##
    def put(self, request, id=None):
        return self.update(request, id) #return the updated object


    ## A delete method ##
    def delete(self, request, id=None):
        return self.destroy(request, id) #return the delete object
     



def homePage(request):
    return render(request, '../templates/home.html', {'title':'Home'})

class IteamPage(generics.GenericAPIView):

    serializer_class = GetInfo_Modelserializers
    queryset = GetInfo.objects.all()

    def get(self,request):

        url = 'https://stgportalone.processonepayments.com/Api/Api/Session/Create?portalOneAuthenticationKey=928DA7CD-7B57-4697-BA84-F50518196329&targetOperation=quickPay'
        articles = GetInfo.objects.all(url)
        serializer = GetInfo_Modelserializers(articles, many=True)
        return Response(serializer.data)


        
        r = request.json.get(url)
        books = r.json()
        books_list = {'books':books['results']}
        return render(request,'books.html',books_list)

class GetInfoVGiewSet(viewsets.ModelViewSet):

    serializer_class = GetInfo_Modelserializers
    queryset = GetInfo.objects.all()

    def list(self, request):
        info = GetInfo.objects.all()
        serializer = GetInfo_Modelserializers(info, many=True)
        
        return Response(serializer.data) #return all the data after serializer
