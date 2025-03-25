from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

"""
    Views Gerais do Projeto
"""
def login_page(request):
    return render(request, 'generic/login.html')

def home(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
    
        #Autenticação
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, 'Login efetuado com sucesso.')
            redirect('home')
        else:
            messages.error(request, 'Usuário ou senha inválidos.')
            return redirect('login')    
        
    else:
        return render(request, 'generic/login.html')

def about(request):
    return render(request, 'generic/about.html')

"""
    Urls do Projeto
"""
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login_page, name='login'), 
    path('home/', home, name='home'),
    path('about/', about, name='about'),
    path('logout/', logout, name='logout'),
    
    # Urls de Apps
    path('recepcao/', include('recepcao.urls')),
]
