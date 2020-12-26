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
import time

# Create your views here.
### a class base data using APIView ###
class ArticleAPIView(APIView):
    ## A get method ##
    lookup_url_kwarg = 'https://stgportalone.processonepayments.com/Api/Api/Session/Create?portalOneAuthenticationKey=0ae16856-aef9-4170-86d6-8d3daa96cd14'
    def get(self, request):
        articles = GetInfo.objects.all()
        serializer = GetInfo_Modelserializers(articles, many=True)
        return Response(serializer.data) #return all the data after serializer



class GenericAPIView(generics.ListAPIView):
    serializer_class = GetInfo_Modelserializers
    queryset = GetInfo.objects.all()
    lookup_url_kwarg = 'https://stgportalone.processonepayments.com/Api/Api/Session/Create?portalOneAuthenticationKey=0ae16856-aef9-4170-86d6-8d3daa96cd14'
    # def get_queryset(self):
    #     queryset = GetInfo.objects.all()
    #     portalOneAuthenticationKey = self.request.query_params.get['PortalOneSessionKey']
    #     queryset = queryset.filter(token = portalOneAuthenticationKey)
    #     return queryset

    ## A get method ##
    def get(self, request, id=None):

        if id:
            return self.retrieve(request)

        else:
            return self.list(request)


@api_view(('GET',))
def external_api_view(request):
    if request.method == "GET":
        r = requests.get("https://stgportalone.processonepayments.com/Api/Api/Session/Create?portalOneAuthenticationKey=0ae16856-aef9-4170-86d6-8d3daa96cd14", timeout=10)
        if r.status_code == 200:
            # data = r.json()
            serializer = GetInfo_Modelserializers(r.json())
            return Response(serializer.data, status=status.HTTP_200_OK)


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
