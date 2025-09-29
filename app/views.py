from django.shortcuts import render
from .models import login, index, agendar
# Create your views here.


def login(request):
    return render(request, 'login.html')

def index(request):
    return render(request, 'index.html')

def agendar(request):
    return render(request, "agendar.html")
