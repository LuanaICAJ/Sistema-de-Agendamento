from django.contrib import admin
from django.urls import path
from app.views import login, index, agdequipamento, reservas, agdSala, editarReserva, deletar_reserva

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login),
    path('index/', index, name="index"),
    path('agdequipamento/', agdequipamento, name="agdequipamento"),
    path('reservas/', reservas, name='reservas'),
    path('agendar-sala/', agdSala, name='sala'),
    path('reservas/editar', editarReserva, name='editar-reserva'),
    path('reservas/deletar/<int:id>/', deletar_reserva, name='deletar-reserva'),
]
