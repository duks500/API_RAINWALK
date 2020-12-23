from django.urls import path, include
from .views import GetInfoVGiewSet, homePage, IteamPage, GetInfoID
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('getInfro', GetInfoID, basename='getInfr')


urlpatterns = [
    path('view/', include(router.urls)),
    path('view/<int:pk>', include(router.urls)),
    # path('', homePage, name='home')
    path('', include(router.urls))
]