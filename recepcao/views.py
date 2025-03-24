from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_recepcao(request):
    return render(request, 'home_recepcao.html') # new