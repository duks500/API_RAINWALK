from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import Article
from .serializers import ArticleSerializer_Modelserializers
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, generics, mixins, viewsets
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class ArticelViewSet(viewsets.ModelViewSet):
    
    serializer_class = ArticleSerializer_Modelserializers ##serilaze the data
    queryset = Article.objects.all() #add all the datas to a query set

# class ArticelViewSet(
#     viewsets.GenericViewSet,
#     mixins.ListModelMixin,
#     mixins.CreateModelMixin,
#     mixins.UpdateModelMixin,
#     mixins.RetrieveModelMixin,
#     mixins.DestroyModelMixin):
    
#     ## Built in variabling into the mixin class ##
#     serializer_class = ArticleSerializer_Modelserializers ##serilaze the data
#     queryset = Article.objects.all() #add all the datas to a query set
    




### A class base data using the Mixins extensions ###
### This is equal to the ArticleAPIView class but as you can tell it is mush easier and much more straight forward ###
class GenericAPIView(
    
    generics.GenericAPIView,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin):

    ## Built in variabling into the mixin class ##
    serializer_class = ArticleSerializer_Modelserializers ##serilaze the data
    queryset = Article.objects.all() #add all the datas to a query set

    lookup_field = 'id' #instead of using pk, I am using an id

    #authentication_classes = [SessionAuthentication, BasicAuthentication] #check for SessionAuthentication and for BasicAuthentication in case SessionAuthentication is not avialable
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]


    ## A get method ##
    def get(self, request, id=None):

        if id:
            return self.retrieve(request)

        else:
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



### a class base data using APIView ###
class ArticleAPIView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication] #check for SessionAuthentication and for BasicAuthentication in case SessionAuthentication is not avialable
    permission_classes = [IsAuthenticated]

    ## A get method ##
    def get(self, request):
        articles = Article.objects.all()
        serializer = ArticleSerializer_Modelserializers(articles, many=True)
        return Response(serializer.data) #return all the data after serializer

    ## A post method ##
    def post(self, request):
        serializer = ArticleSerializer_Modelserializers(data=request.data)

        # if the data is vaild - save the data #
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        # if the data is not vaild - thorugh an error #
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


### a class base data using APIView ###
class ArticleDetails(APIView):


    ## check if the data is avialble ##
    def get_object(self, id):
        ## First check whtere the object has an id ##
        try:
            return Article.objects.get(id=id)
        ## if does not have - the item is not in the system - not found
        except Article.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)


    ## A get function for an existince object with spacific id ##
    def get(self, request, id):
        article = self.get_object(id)
        serializer = ArticleSerializer_Modelserializers(article)
        return Response(serializer.data)


    ## A put function for an existince object with spacific id ##
    def put(self, request, id):
        article = self.get_object(id)
        serializer = ArticleSerializer_Modelserializers(article, data=request.data)

        # if the data is vaild - save the data #
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        # if the data is not vaild - thorugh an error #
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    ## A delete function for an existince object with spacific id ##
    def delete(self, request, id):
        article = self.get_object(id)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



## standart GET and POST new object 
@api_view(['GET' , 'POST'])
def article_list(request):

    ## looking if the request method is equal to Get. If yes, return a list of all the objects ##
    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticleSerializer_Modelserializers(articles, many=True)
        return Response(serializer.data) #return all the data after serializer
    
    ## looking if the request method is equal to Post. If yes, send the require data to the serializer ##
    elif request.method == 'POST':
        serializer = ArticleSerializer_Modelserializers(data=request.data)

        # if the data is vaild - save the data #
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        # if the data is not vaild - thorugh an error #
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


## standart GET, PUT, and DELETE an exsistance object
@api_view(['GET' , 'PUT' , 'DELETE'])
def article_detail(request, pk):

    ## First check whtere the object has a pk ##
    try:
        article = Article.objects.get(pk=pk)
    ## if does not have - the item is not in the system - not found
    except Article.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    ## if the request method is GET, return the information of the spacific object ##
    if request.method == 'GET':
        serializer = ArticleSerializer_Modelserializers(article)
        return Response(serializer.data)

    ## if the request method is PUT, update the required object ##
    elif request.method == 'PUT':
        serializer = ArticleSerializer_Modelserializers(article, data=request.data)

        # if the data is vaild - save the data #
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        # if the data is not vaild - thorugh an error #
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    ## if the request method is DELETE, delete the required object ##
    elif request.method == 'DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)