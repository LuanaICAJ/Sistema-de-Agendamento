from django.contrib import admin
from django.urls import path
from app import views
from app.views import login, index, agdequipamento, reservas, agdSala, editarReserva, deletar_reserva

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login),
    path('index/', index, name="index"),
    path('agdequipamento/', agdequipamento, name="agdequipamento"),
    path('reservas/', reservas, name='reservas'),
    path('agendar-sala/', agdSala, name='sala'),
    path('reservas/sala/editar/<int:pk>/', views.editar_reserva_sala, name='editar_reserva_sala'),
    path('reservas/equipamento/editar/<int:pk>/', views.editar_reserva_equipamento, name='editar_reserva_equipamento'),
    path('reservas/deletar/<int:id>/', deletar_reserva, name='deletar-reserva'),
]
