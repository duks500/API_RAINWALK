from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import Article
from .serializers import ArticleSerializer_Modelserializers
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

@csrf_exempt
def article_list(request):

    ## looking if the request method is equal to Get. If yes, return a list of all the objects ##
    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticleSerializer_Modelserializers(articles, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    ## looking if the request method is equal to Post. If yes, send the require data to the serializer ##
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ArticleSerializer_Modelserializers(data=data)

        # if the data is vaild - save the data #
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        
        # if the data is not vaild - thorugh an error #
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def srticle_detail(request, pk):

    ## First check whtere the object has a pk ##
    try:
        article = Article.objects.get(pk=pk)
    ## if does not have - the item is not in the system - not found
    except Article.DoesNotExist:
        return HttpResponse(status=404)

    ## if the request method is GET, return the information of the spacific object ##
    if request.method == 'GET':
        serializer = ArticleSerializer_Modelserializers(article)
        return JsonResponse(serializer.data)

    ## if the request method is PUT, update the required object ##
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ArticleSerializer_Modelserializers(article, data=data)

        # if the data is vaild - save the data #
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)

        # if the data is not vaild - thorugh an error #
        return JsonResponse(serializer.errors, status=400)

    ## if the request method is DELETE, delete the required object ##
    elif request.method == 'DELETE':
        article.delete()
        return HttpResponse(status=204)