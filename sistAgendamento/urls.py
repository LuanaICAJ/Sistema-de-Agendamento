from django.contrib import admin
from django.urls import path
from app import views
from app.views import user_login, index, agdequipamento, reservas, agdSala, user_logout, index_adm

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.user_login, name='login'),
    path('index/', index, name="index"),
    path('agdequipamento/', agdequipamento, name="agdequipamento"),
    path('reservas/', reservas, name='reservas'),
    path('agendar-sala/', agdSala, name='sala'),
    path('reservas/sala/editar/<int:pk>/', views.editar_reserva_sala, name='editar_reserva_sala'),
    path('reservas/equipamento/editar/<int:pk>/', views.editar_reserva_equipamento, name='editar_reserva_equipamento'),
    path('reservas/sala/deletar/<int:pk>/', views.deletar_reserva_sala, name='deletar_reserva_sala'),
    path('reservas/equipamento/deletar/<int:pk>/', views.deletar_reserva_equipamento, name='deletar_reserva_equipamento'),
    path('logout/', views.user_logout, name='logout'),
    path('index_adm/', views.index_adm, name="index_adm"),
    path('cadastrar_equipamento/', views.CadastrarEquipamento, name="cadastrar_equipamento"),
    path('cadastrar_sala/', views.CadastrarSala, name="cadastrar_sala"),
]
