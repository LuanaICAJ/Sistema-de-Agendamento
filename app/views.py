from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from .models import (
    index, agdequipamento, reservas, agdSala, 
    Equipamento, Sala, ReservaSala, ReservaEquipamento
)

from datetime import date

# Create your views here.

def user_login(request): 
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        
        if user is not None:
            auth_login(request, user)
            messages.success(request, 'Login realizado com sucesso!')
            return redirect('index') 
        else:
            messages.error(request, 'Email ou senha inválidos.')      
    return render(request, 'login.html')

@login_required
def index(request):
    return render(request, 'index.html')

@login_required
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


@login_required
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

@login_required
def reservas(request):
    reservasSala = ReservaSala.objects.all().order_by('-data', '-hora_inicio', '-hora_fim')
    reservasEquipamento = ReservaEquipamento.objects.all().order_by('-data', '-hora_inicio', '-hora_fim')
    return render(request, 'reservas.html', {'reservaSala': reservasSala, 'reservaEquipamento': reservasEquipamento })

@login_required
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

@login_required
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

@login_required
def deletar_reserva_sala(request, pk):
    reserva = get_object_or_404(ReservaSala, pk=pk)
    if request.method == 'POST':
        reserva.delete()
        messages.success(request, 'Reserva de sala excluída com sucesso!')
        return redirect('reservas')
    return render(request, 'deletar_reserva.html', {'reserva': reserva})

@login_required
def deletar_reserva_equipamento(request, pk):
    reserva = get_object_or_404(ReservaEquipamento, pk=pk)
    if request.method == 'POST':
        reserva.delete()
        messages.success(request, 'Reserva de equipamento excluída com sucesso!')
        return redirect('reservas')
    return render(request, 'deletar_reserva.html', {'reserva': reserva})

@login_required
def index_adm(request):
    return render(request, 'index_adm.html')

@login_required
def user_logout(request): # Função para deslogar o usuário
    auth_logout(request)
    messages.info(request, "Você foi desconectado com sucesso.")
    return redirect('login')

@login_required
def CadastrarEquipamento(request):
    if request.method == 'POST':
        # Capturar os dados do formulário
        tipo = request.POST.get('tipo')
        statusDisponibilidade = request.POST.get('statusDisponibilidade')

        # Criar o novo objeto Equipamento
        Equipamento.objects.create(
            tipo=tipo,
            statusDisponibilidade=statusDisponibilidade,
        )
        
        messages.success(request, f'O equipamento "{tipo}" foi cadastrado com sucesso!')

        # Redirecionar para a página
        return redirect('cadastrar_equipamento')
        
    return render(request, 'cadastrar_equipamento.html')

@login_required
def CadastrarSala(request):
    if request.method == 'POST':
        # Capturar os dados do formulário
        nome = request.POST.get('nome')
        capacidade = request.POST.get('capacidade')
        statusDisponibilidade = request.POST.get('statusDisponibilidade')

        # Criar o novo objeto Equipamento
        Sala.objects.create(
            nome=nome,
            capacidade=capacidade,
            statusDisponibilidade=statusDisponibilidade,
        )
        
        messages.success(request, f'A sala "{nome}" foi cadastrada com sucesso!')

        # Redirecionar para a página
        return redirect('listar_salas')
        
    return render(request, 'cadastrar_sala.html')

@login_required
def reserva_for_adms(request):
    reservasSala = ReservaSala.objects.all().order_by('-data', '-hora_inicio', '-hora_fim')
    reservasEquipamento = ReservaEquipamento.objects.all().order_by('-data', '-hora_inicio', '-hora_fim')
    return render(request, 'reserva_for_adms.html', {'reservaSala': reservasSala, 'reservaEquipamento': reservasEquipamento})

@login_required
def listarSalas(request):
    listarSalas = Sala.objects.all()
    return render (request, 'listar_salas.html', {'listarSalas':listarSalas})

@login_required
def listarEquipamentos(request):
    listarEquipamentos = Equipamento.objects.all()
    return render (request, 'listar_equipamentos.html', {'listarEquipamentos':listarEquipamentos})

@login_required
def deletar_sala (request, pk):
    sala = get_object_or_404(Sala, pk=pk)
    if request.method == 'POST':
        sala.delete()
        messages.success(request, 'Sala excluída com sucesso!')
        return redirect('listar_salas')
    return render(request, 'deletar_sala.html', {'sala': sala})

@login_required
def deletar_equipamento (request, pk):
    equipamento = get_object_or_404(Equipamento, pk=pk)
    if request.method == 'POST':
        equipamento.delete()
        messages.success(request, 'Equipamento excluído com sucesso!')
        return redirect('listar_equipamentos')
    return render(request, 'deletar_equipamento.html', {'equipamento': equipamento})

@login_required
def editar_sala(request, pk):
    sala = get_object_or_404(Sala, pk=pk)
    if request.method == 'POST':
        sala.nome = request.POST.get('nome')
        sala.capacidade = request.POST.get('capacidade')
        sala.statusDisponibilidade = request.POST.get('statusDisponibilidade')
        sala.save()
        messages.success(request, 'Cadastro de sala atualizado com sucesso!')
        return redirect('listar_salas')
    return render(request, 'editar_sala.html', {'sala': sala})

@login_required
def editar_equipamento(request, pk):
    equipamento = get_object_or_404(Equipamento, pk=pk)
    if request.method == 'POST':
        equipamento.tipo = request.POST.get('tipo')
        equipamento.statusDisponibilidade = request.POST.get('statusDisponibilidade')
        equipamento.save()
        messages.success(request, 'Cadastro de equipamento atualizado com sucesso!')
        return redirect('listar_equipamentos')
    return render(request, 'editar_equipamento.html', {'equipamento': equipamento})