import os
import sys

# adiciona o diretório raiz (onde está manage.py) ao caminho do Python
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from app.models import Equipamento, Sala, ReservaEquipamento, ReservaSala


import pytest
from django.urls import reverse
from app.models import Equipamento, Sala, ReservaEquipamento, ReservaSala


@pytest.fixture
def equipamento():
    return Equipamento.objects.create(
        idEquipamento=1,
        tipo="Projetor",
        statusDisponibilidade="disponível"
    )

@pytest.fixture
def sala():
    return Sala.objects.create(
        idSala=1,
        nome="Sala 101",
        capacidade=20,  
        statusDisponibilidade="disponível"
    )

@pytest.fixture
def client_logged(client):
    # Caso tenha autenticação futuramente
    return client
