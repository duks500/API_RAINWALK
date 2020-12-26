from django.urls import path, include
from .views import GetInfoVGiewSet, homePage, IteamPage, GetInfoID, external_api_view, GenericAPIView, ArticleAPIView, Getting_Session_Id, Creating_Account
from rest_framework.routers import DefaultRouter
#Creating_Account


router = DefaultRouter()
# router.register('getInfro', GetInfoID, basename='getInfr')
router.register('getInfro', Getting_Session_Id, basename='getInfr')

routerPOST = DefaultRouter()
routerPOST.register('create', Creating_Account, basename='create')

urlpatterns = [
    # path('view/', include(router.urls)),
    # path('view/<int:pk>', include(router.urls)),
    # path('', homePage, name='home')
    # path('', include(router.urls)),
    path('ext/', external_api_view),
    # path('', GenericAPIView.as_view()),
    path('t', ArticleAPIView.as_view()),
    path('', include(router.urls)),
    path('create/', include(routerPOST.urls)),
]