import pytest
from django.urls import reverse
from app.models import ReservaSala

@pytest.mark.django_db
def test_agdsala_post_sucesso(client, sala):
    url = reverse('sala')
    data = {
        'sala': sala.idSala,
        'data': '2025-10-15',
        'hora_inicio': '14:00',
        'hora_fim': '15:00'
    }
    response = client.post(url, data, follow=True)
    assert response.status_code == 200
    assert ReservaSala.objects.count() == 1
    reserva = ReservaSala.objects.first()
    assert reserva.sala == sala
