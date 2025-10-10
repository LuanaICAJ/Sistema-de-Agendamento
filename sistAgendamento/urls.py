from django.contrib import admin
from django.urls import path
from app.views import login, index, agdequipamento, reservas, agdSala, editarReserva

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login),
    path('index/', index, name="index"),
    path('agdequipamento/', agdequipamento, name="agdequipamento"),
    path('reservas', reservas, name='reservas'),
    path('agendar-sala', agdSala, name='sala'),
    path('editar', editarReserva, name='editar-reserva')
]
