import pytest
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import date, timedelta, time

from app.models import Equipamento, Sala, ReservaEquipamento, ReservaSala

@pytest.fixture
def usuario_logado(db, client):
    user = User.objects.create_user(
        username="teste",
        password="12345"
    )
    client.login(username="teste", password="12345")
    return client


@pytest.fixture
def equipamento():
    return Equipamento.objects.create(
        tipo="Projetor",
        statusDisponibilidade="disponível"
    )


@pytest.fixture
def sala():
    return Sala.objects.create(
        nome="Laboratório 1",
        capacidade=30,
        statusDisponibilidade="disponível"
    )


def test_get_agdequipamento(usuario_logado):
    url = reverse("agdequipamento")
    response = usuario_logado.get(url)
    assert response.status_code == 200


def test_criar_reserva_equipamento(usuario_logado, equipamento):
    url = reverse("agdequipamento")
    data_futura = date.today() + timedelta(days=1)

    response = usuario_logado.post(url, data={
        "equipamento": equipamento.pk,
        "data": data_futura,
        "hora_inicio": "10:00",
        "hora_fim": "11:00",
    })

    assert response.status_code == 302
    assert ReservaEquipamento.objects.count() == 1


def test_nao_permite_data_passada(usuario_logado, equipamento):
    url = reverse("agdequipamento")
    data_passada = date.today() - timedelta(days=1)

    response = usuario_logado.post(url, data={
        "equipamento": equipamento.pk,
        "data": data_passada,
        "hora_inicio": "10:00",
        "hora_fim": "11:00",
    })

    assert response.status_code == 200
    assert ReservaEquipamento.objects.count() == 0


def test_conflito_reserva(usuario_logado, equipamento):
    data_futura = date.today() + timedelta(days=1)

    ReservaEquipamento.objects.create(
        equipamento=equipamento,
        data=data_futura,
        hora_inicio=time(10, 0),
        hora_fim=time(11, 0),
        status="confirmado"
    )

    url = reverse("agdequipamento")
    response = usuario_logado.post(url, data={
        "equipamento": equipamento.pk,
        "data": data_futura,
        "hora_inicio": "10:00",
        "hora_fim": "11:00",
    })

    assert response.status_code == 200
    assert ReservaEquipamento.objects.count() == 1


def test_criar_reserva_sala(usuario_logado, sala):
    url = reverse("sala")
    data_futura = date.today() + timedelta(days=1)

    response = usuario_logado.post(url, data={
        "sala": sala.pk,
        "data": data_futura,
        "hora_inicio": "08:00",
        "hora_fim": "09:00",
    })

    assert response.status_code == 302
    assert ReservaSala.objects.count() == 1


def test_editar_reserva_equipamento(usuario_logado, equipamento):
    data_futura = date.today() + timedelta(days=1)
    reserva = ReservaEquipamento.objects.create(
        equipamento=equipamento,
        data=data_futura,
        hora_inicio="10:00",
        hora_fim="11:00",
        status="confirmado"
    )

    url = reverse("editar_reserva_equipamento", args=[reserva.pk])
    response = usuario_logado.post(url, data={
        "data": data_futura,
        "hora_inicio": "12:00",
        "hora_fim": "13:00",
    })

    reserva.refresh_from_db()
    assert response.status_code == 302
    assert reserva.hora_inicio == time(12, 0)


def test_deletar_reserva_equipamento(usuario_logado, equipamento):
    data_futura = date.today() + timedelta(days=1)
    reserva = ReservaEquipamento.objects.create(
        equipamento=equipamento,
        data=data_futura,
        hora_inicio="10:00",
        hora_fim="11:00",
        status="confirmado"
    )

    url = reverse("deletar_reserva_equipamento", args=[reserva.pk])
    response = usuario_logado.post(url)

    assert response.status_code == 302
    assert ReservaEquipamento.objects.count() == 0
