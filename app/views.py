from django.shortcuts import redirect, render
from .models import login, index, agdequipamento, reservas, agdSala, Equipamento,Sala, ReservaSala,ReservaEquipamento
from django.contrib import messages
from datetime import date


from app.models import ReservaSala,ReservaEquipamento, Equipamento,Sala
# Create your views here.


def login(request):
    return render(request, 'login.html')

def index(request):
    return render(request, 'index.html')

def agdequipamento(request):
    if request.method == 'POST':
        equipamento_id = request.POST.get('equipamento')
        data = request.POST.get('data')
        hora = request.POST.get('hora')

        equipamento = Equipamento.objects.get(idEquipamento=equipamento_id)

        # Verifica se o equipamento já está reservado neste dia e hora
        conflito = ReservaEquipamento.objects.filter(equipamento=equipamento, data=data, hora=hora).exists()
        if conflito:
            messages.error(request, 'Este equipamento já está reservado nesse horário!')
        else:
            ReservaEquipamento.objects.create(
                equipamento=equipamento,
                data=data,
                hora=hora,
                status='confirmado'
            )
            equipamento.statusDisponibilidade = 'indisponível'
            equipamento.save()
            messages.success(request, 'Reserva feita com sucesso!')
            return redirect('reservas')
        
    equipamento = Equipamento.objects.all()
    return render(request, 'agdequipamento.html', {'equipamentos': equipamento})


def reservas(request):
    reservasSala = ReservaSala.objects.all().order_by('-data', '-hora')
    reservasEquipamento = ReservaEquipamento.objects.all().order_by('-data', '-hora')
    return render(request, 'reservas.html', {'reservaSala': reservasSala, 'reservaEquipamento': reservasEquipamento })


def agdSala(request):
    if request.method == 'POST':
        sala_id = request.POST.get('sala')
        data = request.POST.get('data')
        hora = request.POST.get('hora')

        sala = Sala.objects.get(idSala=sala_id)

        # Verifica se o equipamento já está reservado neste dia e hora
        conflito = ReservaSala.objects.filter(sala=sala, data=data, hora=hora).exists()
        if conflito:
            messages.error(request, 'Esta sala já está reservada nesse horário!')
        else:
            ReservaSala.objects.create(
                sala=sala,
                data=data,
                hora=hora,
                status='confirmado'
            )
            sala.statusDisponibilidade = 'indisponível'
            sala.save()
            messages.success(request, 'Reserva feita com sucesso!')
            return redirect('reservas')
        
    salas =  Sala.objects.all()

    return render(request, 'agdSala.html', {'salas': salas})

