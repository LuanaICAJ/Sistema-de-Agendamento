from django.contrib import admin
from django.urls import path
from app.views import login, index, agdequipamento, reservas, agdSala

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login),
    path('index/', index, name="index"),
    path('agdequipamento/', agdequipamento, name="agdequipamento"),
    path('reservas', reservas, name='reservas'),
    path('agendar-sala', agdSala, name='sala'),
]
