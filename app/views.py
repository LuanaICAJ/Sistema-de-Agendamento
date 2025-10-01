from django.shortcuts import render
from .models import login, index, agdequipamento
# Create your views here.


def login(request):
    return render(request, 'login.html')

def index(request):
    return render(request, 'index.html')

def agdequipamento(request):
    return render(request, "agdequipamento.html")
