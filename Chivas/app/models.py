from django.db import models

# Create your models here.
class Viajes(models.Model):
    destino = models.CharField(max_length=30)
    fecha_salida = models.CharField(max_length=20)
    asientos_disponibles = models.PositiveIntegerField()
    estado_actual = models.CharField(max_length=10)
    chiva_asignada = models.CharField(max_length=20)
    precio_asiento = models.FloatField() 
    conductor_asignado = models.CharField(max_length=20)

    def __str__(self):
        return f'Destino: {self.destino}, salida: {self.fecha_salida}, precio: {self.precio_asiento}.'