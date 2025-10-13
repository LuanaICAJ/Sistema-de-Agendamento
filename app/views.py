from django.shortcuts import get_object_or_404, redirect, render
from .models import login, index, agdequipamento, reservas, agdSala, Equipamento,Sala, ReservaSala,ReservaEquipamento, editarReserva
from django.contrib import messages
from datetime import date


from app.models import ReservaSala,ReservaEquipamento, Equipamento,Sala
# Create your views here.

def editarReserva(request):
    return render (request, 'editarReserva.html')

def login(request):
    return render(request, 'login.html')

def index(request):
    return render(request, 'index.html')

def agdequipamento(request):
    if request.method == 'POST':
        equipamento_id = request.POST.get('equipamento')
        data = request.POST.get('data')
        hora_inicio = request.POST.get('hora_inicio')
        hora_fim = request.POST.get('hora_final')

        equipamento = Equipamento.objects.get(idEquipamento=equipamento_id)

        # Verifica se o equipamento já está reservado neste dia e hora
        conflito = ReservaEquipamento.objects.filter(equipamento=equipamento, data=data, hora_inicio=hora_inicio, hora_fim= hora_fim).exists()
        if conflito:
            messages.error(request, 'Este equipamento já está reservado nesse horário!')
        else:
            ReservaEquipamento.objects.create(
                equipamento = equipamento,
                data = data,
                hora_inicio = hora_inicio,
                hora_fim = hora_fim,
                status ='confirmado'
            )
            equipamento.statusDisponibilidade = 'indisponível'
            equipamento.save()
            messages.success(request, 'Reserva feita com sucesso!')
            return redirect('reservas')
        
    equipamento = Equipamento.objects.all()
    return render(request, 'agdequipamento.html', {'equipamentos': equipamento})


def reservas(request):
    reservasSala = ReservaSala.objects.all().order_by('-data', '-hora_inicio', '-hora_fim')
    reservasEquipamento = ReservaEquipamento.objects.all().order_by('-data', '-hora_inicio', '-hora_fim')
    return render(request, 'reservas.html', {'reservaSala': reservasSala, 'reservaEquipamento': reservasEquipamento })


def agdSala(request):
    if request.method == 'POST':
        sala_id = request.POST.get('sala')
        data = request.POST.get('data')
        hora_inicio = request.POST.get('hora_inicio')
        hora_fim = request.POST.get('hora_fim')
        
        sala = Sala.objects.get(idSala=sala_id)

        # Verifica se o equipamento já está reservado neste dia e hora
        conflito = ReservaSala.objects.filter(sala=sala, data=data, hora_inicio=hora_inicio, hora_fim=hora_fim).exists()
        if conflito:
            messages.error(request, 'Esta sala já está reservada nesse horário!')
        else:
            ReservaSala.objects.create(
                sala = sala,
                data = data,
                hora_inicio = hora_inicio,
                hora_fim = hora_fim,
                status ='confirmado'
            )
            sala.statusDisponibilidade = 'indisponível'
            sala.save()
            messages.success(request, 'Reserva feita com sucesso!')
            return redirect('reservas')
        
    salas =  Sala.objects.all()

    return render(request, 'agdSala.html', {'salas': salas})

def deletar_reserva(request, pk):
    sala = get_object_or_404(sala, pk=pk)
    if request.method == 'POST':
        sala.delete()
        return redirect('reservas')
    return render(request, 'deletar_sala.html', {'Reserva': sala})

