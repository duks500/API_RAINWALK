from django.urls import path, include
from .views import GetInfoVGiewSet, homePage, IteamPage, GetInfoID, external_api_view, GenericAPIView, ArticleAPIView
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('getInfro', GetInfoID, basename='getInfr')


urlpatterns = [
    path('view/', include(router.urls)),
    path('view/<int:pk>', include(router.urls)),
    # path('', homePage, name='home')
    # path('', include(router.urls)),
    path('ext/', external_api_view),
    path('', GenericAPIView.as_view()),
    path('t', ArticleAPIView.as_view())
]