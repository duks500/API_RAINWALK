from django.urls import path, include
from new.api.views import api_detail_view


urlpatterns = [
    path('', api_detail_view, name='detail')
]