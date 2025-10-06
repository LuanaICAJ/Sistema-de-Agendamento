from django.shortcuts import render
from .models import login, index, agdequipamento, reservas, Reserva, agdSala, Equipamento,Sala

from app.models import Reserva, Equipamento,Sala
# Create your views here.


def login(request):
    return render(request, 'login.html')

def index(request):
    return render(request, 'index.html')

def agdequipamento(request):
    dados = {'lista_equipamento': Equipamento.objects.all()}
    return render(request, 'agdequipamento.html',dados)

def reservas(request):
    dados = {'lista_reservas': Reserva.objects.all()}
    return render(request, 'reservas.html', dados)

def agdSala(request):
    dados = {'lista_sala': Sala.objects.all()}
    return render(request, 'agdSala.html',dados)
