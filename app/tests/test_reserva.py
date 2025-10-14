import pytest
from django.urls import reverse
from app.models import ReservaEquipamento

@pytest.mark.django_db
def test_agdequipamento_get(client):
    """Testa se o GET da página de agendamento de equipamento renderiza corretamente."""
    url = reverse('agdequipamento')
    response = client.get(url)
    assert response.status_code == 200
    assert 'equipamentos' in response.context


@pytest.mark.django_db
def test_agdequipamento_post_sucesso(client, equipamento):
    """Testa se uma reserva de equipamento é criada com sucesso."""
    url = reverse('agdequipamento')
    data = {
        'equipamento': equipamento.idEquipamento,
        'data': '2025-10-15',
        'hora_inicio': '08:00',
        'hora_fim': '10:00'
    }
    response = client.post(url, data, follow=True)
    assert response.status_code == 200
    assert ReservaEquipamento.objects.count() == 1
    reserva = ReservaEquipamento.objects.first()
    assert reserva.equipamento == equipamento
    assert reserva.status == 'confirmado'


@pytest.mark.django_db
def test_agdequipamento_post_conflito(client, equipamento):
    """Testa se impede reserva quando já existe uma no mesmo horário."""
    ReservaEquipamento.objects.create(
        equipamento=equipamento,
        data='2025-10-15',
        hora_inicio='08:00',
        hora_fim='10:00',
        status='confirmado'
    )
    url = reverse('agdequipamento')
    data = {
        'equipamento': equipamento.idEquipamento,
        'data': '2025-10-15',
        'hora_inicio': '08:00',
        'hora_fim': '10:00'
    }
    response = client.post(url, data)
    # A página recarrega sem criar nova reserva
    assert ReservaEquipamento.objects.count() == 1
    assert response.status_code == 200
