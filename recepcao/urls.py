from django.urls import path
from django.http import HttpResponse
from recepcao.views import home_recepcao

app_name = 'recepcao'

urlpatterns = [
    path('', home_recepcao, name='home_recepcao'),
]