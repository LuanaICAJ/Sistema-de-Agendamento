import pytest
from django.contrib.auth.models import User

@pytest.fixture
def usuario_logado(db, client):
    user = User.objects.create_user(
        username="testuser",
        password="12345"
    )
    client.login(username="testuser", password="12345")
    return client
