from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from .models import (
    login, index, agdequipamento, reservas, agdSala, 
    Equipamento, Sala, ReservaSala, ReservaEquipamento
)

from datetime import date

# Create your views here.

def login(request):
    return render(request, 'login.html')

def index(request):
    return render(request, 'index.html')

def agdequipamento(request):
    if request.method == 'POST':
        equipamento_id = request.POST.get('equipamento')
        data = request.POST.get('data')
        hora_inicio = request.POST.get('hora_inicio')
        hora_fim = request.POST.get('hora_fim')

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

def reservas(request):
    reservasSala = ReservaSala.objects.all().order_by('-data', '-hora_inicio', '-hora_fim')
    reservasEquipamento = ReservaEquipamento.objects.all().order_by('-data', '-hora_inicio', '-hora_fim')
    return render(request, 'reservas.html', {'reservaSala': reservasSala, 'reservaEquipamento': reservasEquipamento })

def editar_reserva_sala(request, pk):
    reserva = get_object_or_404(ReservaSala, pk=pk)
    if request.method == 'POST':
        reserva.data = request.POST.get('data')
        reserva.hora_inicio = request.POST.get('hora_inicio')
        reserva.hora_fim = request.POST.get('hora_fim')
        reserva.save()
        messages.success(request, 'Reserva de sala atualizada com sucesso!')
        return redirect('reservas')
    return render(request, 'editar_reserva_sala.html', {'reserva': reserva})

def editar_reserva_equipamento(request, pk):
    reserva = get_object_or_404(ReservaEquipamento, pk=pk)
    if request.method == 'POST':
        reserva.data = request.POST.get('data')
        reserva.hora_inicio = request.POST.get('hora_inicio')
        reserva.hora_fim = request.POST.get('hora_fim')
        reserva.save()
        messages.success(request, 'Reserva de equipamento atualizada com sucesso!')
        return redirect('reservas')
    return render(request, 'editar_reserva_equipamento.html', {'reserva': reserva})

def deletar_reserva_sala(request, pk):
    reserva = get_object_or_404(ReservaSala, pk=pk)
    if request.method == 'POST':
        reserva.delete()
        messages.success(request, 'Reserva de sala excluída com sucesso!')
        return redirect('reservas')
    return render(request, 'deletar_reserva.html', {'reserva': reserva})

def deletar_reserva_equipamento(request, pk):
    reserva = get_object_or_404(ReservaEquipamento, pk=pk)
    if request.method == 'POST':
        reserva.delete()
        messages.success(request, 'Reserva de equipamento excluída com sucesso!')
        return redirect('reservas')
    return render(request, 'deletar_reserva.html', {'reserva': reserva})