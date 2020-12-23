from django.shortcuts import render,redirect
from .serializers import GetInfo_Modelserializers



def get_information(portalOneAuthenticationKey, targetOperation):
    url = 'https://stgportalone.processonepayments.com/Api/Api/Session/Create?'
    params = {'portalOneAuthenticationKey': portalOneAuthenticationKey, 'targetOperation': targetOperation}
    r = request.get(url, params=params)
    item = GetInfo_Modelserializers(r.data)
    item_list = {'item':item['results']}
    return item_list


# def get_books(year, author):
#     url = 'http://api.example.com/books' 
#     params = {'year': year, 'author': author}
#     r = requests.get(url, params=params)
#     books = r.json()
#     books_list = {'books':books['results']}
#     return books_list