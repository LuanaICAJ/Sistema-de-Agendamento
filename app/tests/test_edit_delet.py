import pytest
from django.urls import reverse
from app.models import ReservaEquipamento

@pytest.mark.django_db
def test_editar_reserva_equipamento(client, equipamento):
    reserva = ReservaEquipamento.objects.create(
        equipamento=equipamento,
        data='2025-10-15',
        hora_inicio='08:00',
        hora_fim='09:00',
        status='confirmado'
    )
    url = reverse('editar_reserva_equipamento', args=[reserva.pk])
    data = {'data': '2025-10-16', 'hora_inicio': '10:00', 'hora_fim': '11:00'}
    response = client.post(url, data, follow=True)
    reserva.refresh_from_db()
    assert reserva.data.strftime('%Y-%m-%d') == '2025-10-16'
    assert response.status_code == 200


@pytest.mark.django_db
def test_deletar_reserva_equipamento(client, equipamento):
    reserva = ReservaEquipamento.objects.create(
        equipamento=equipamento,
        data='2025-10-15',
        hora_inicio='08:00',
        hora_fim='09:00',
        status='confirmado'
    )
    url = reverse('deletar_reserva_equipamento', args=[reserva.pk])
    response = client.post(url, follow=True)
    assert ReservaEquipamento.objects.count() == 0
    assert response.status_code == 200
