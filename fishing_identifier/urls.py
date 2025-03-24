from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render # new

"""
    Views Gerais do Projeto
"""
def login_view(request):
    return render(request, 'generic/login.html')

def home_view(request):
    return render(request, 'generic/home.html')

def about_view(request):
    return render(request, 'generic/about.html')

"""
    Urls do Projeto
"""
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login_view, name='login'), 
    path('home/', home_view, name='home'),
    path('about/', about_view, name='about'),
    
    # Urls de Apps
    path('recepcao/', include('recepcao.urls')),
]
