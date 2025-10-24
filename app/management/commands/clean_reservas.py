from django.core.management.base import BaseCommand
from datetime import date
from app.models import ReservaSala, ReservaEquipamento 

class Command(BaseCommand):
    help = 'Deleta reservas de salas e equipamentos que já passaram.'

    def handle(self, *args, **options):
        hoje = date.today()
        
        # Deleta reservas de salas com data anterior a hoje
        deleted_salas, _ = ReservaSala.objects.filter(data__lt=hoje).delete()
        
        # Deleta reservas de equipamentos com data anterior a hoje
        deleted_equipamentos, _ = ReservaEquipamento.objects.filter(data__lt=hoje).delete()
        
        self.stdout.write(self.style.SUCCESS(
            f'Sucesso! {deleted_salas} reservas de salas e {deleted_equipamentos} reservas de equipamentos deletadas.'
        ))