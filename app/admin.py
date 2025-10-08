from django.contrib import admin
from app.models import Equipamento, Sala, ReservaSala, ReservaEquipamento
# Register your models here.

admin.site.register(Equipamento)
admin.site.register(Sala)
admin.site.register(ReservaSala)
admin.site.register(ReservaEquipamento)