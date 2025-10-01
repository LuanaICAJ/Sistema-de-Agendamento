from django.db import models

# Create your models here.

class login(models.Model):
    def __str__(self):
        return 
    
class index(models.Model):
    def __str__(self):
        return 
    
class agdequipamento(models.Model):
    def __str__(self):
        return 
    

    
class Equipamento(models.Model):
    idEquipamento = models.IntegerField(primary_key=True)
    tipo = models.CharField(max_length=50, blank=False)
    statusDisponibilidade = models.CharField(max_length=50, blank=False)
    
class Sala(models.Model):
    idSala = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=100, blank=False)
    capacidade = models.IntegerField(blank=False)
    statusDisponibilidade = models.CharField(max_length=50, blank=False)
    
class Reserva(models.Model):
    idReserva = models.IntegerField
    data = models.DateField
    hora = models.TimeField
    status = models.CharField(max_length=50)
    Equipamento = models.ForeignKey(Equipamento, on_delete = models.PROTECT)
    Sala = models.ForeignKey(Sala, on_delete = models.PROTECT)