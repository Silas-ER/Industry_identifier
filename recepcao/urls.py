from django.urls import path
from django.http import HttpResponse
from recepcao.views import home_recepcao

urlpatterns = [
    path('', home_recepcao),
]