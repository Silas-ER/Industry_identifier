from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render # new

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('recepcao.urls')), # new
]
