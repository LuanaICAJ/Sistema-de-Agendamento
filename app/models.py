from django.db import models

# Create your models here.

class Equipamento(models.Model):
    idEquipamento = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=50)
    statusDisponibilidade = models.CharField(max_length=50, default='disponível')

    def __str__(self):
        return self.tipo


class Sala(models.Model):
    idSala = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    capacidade = models.IntegerField()
    statusDisponibilidade = models.CharField(max_length=50, default='disponível')

    def __str__(self):
        return self.nome

class ReservaSala(models.Model):
    sala = models.ForeignKey(Sala, on_delete=models.PROTECT)
    data = models.DateField()
    hora = models.TimeField()
    status = models.CharField(max_length=50, default='confirmado')

    def __str__(self):
        return f"Sala: {self.sala} ({self.data} {self.hora})"


class ReservaEquipamento(models.Model):
    equipamento = models.ForeignKey(Equipamento, on_delete=models.PROTECT)
    data = models.DateField()
    hora = models.TimeField()
    status = models.CharField(max_length=50, default='confirmado')

    def __str__(self):
        return f"Equipamento: {self.equipamento} ({self.data} {self.hora})"

class login(models.Model):
    def __str__(self):
        return 
    
class index(models.Model):
    def __str__(self):
        return 
    
class agdequipamento(models.Model):
    def __str__(self):
        return 

class reservas(models.Model):
    def __str__(self):
        return
    
class agdSala(models.Model):
    def __str__(self):
        return