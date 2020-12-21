from django.urls import path
from .views import article_list, srticle_detail

urlpatterns = [
    path('article/', article_list),
    path('detail/<int:pk>', srticle_detail),
]
