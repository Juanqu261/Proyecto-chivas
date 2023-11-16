from django.db import models

# Create your models here.
class Viajes(models.Model):
    destino = models.CharField(max_length=30)
    fecha_salida = models.CharField(max_length=20)
    asientos_disponibles = models.PositiveIntegerField()
    estado_actual = models.CharField(max_length=10)
    #0: Indica terminado
    #1: Indica disponible
    chiva_asignada = models.CharField(max_length=20)
    precio_asiento = models.FloatField() 
    conductor_asignado = models.CharField(max_length=20)

    def __str__(self):
        return f'Destino: {self.destino}, salida: {self.fecha_salida}, precio: {self.precio_asiento}.'
    
class Reservas(models.Model):
    viaje_reservado = models.CharField(max_length=20) #id del viaje reservado o matricula de chiva reservada
    asientos_reservados = models.CharField(max_length=2)
    nombre_titular = models.CharField(max_length=30)
    identificacion_titular = models.CharField(max_length=15)
    email_titular = models.CharField(max_length=20)
    celular_titular = models.CharField(max_length=10)
    direccion_titular = models.CharField(max_length=30)

class Chivas(models.Model):
    matricula = models.CharField(max_length=20) #chiva_asignada para otros campos
    tecnomecanica = models.CharField(max_length=20) #Fecha maxima de cumplimiento de la tecnomecanica actual
    numero_poliza = models.CharField(max_length=20)
    reporte_daño = models.CharField(max_length=40) #Breve descripcion de posibles daños, de lo contrario: 0
    estado = models.CharField(max_length=10)
    #Estados de la chiva:
    #-1: Indica daños reportados o tecnomecanica vencida
    # 0: Indica que la chiva esta en uso
    # 1: Indica que la chiva esta disponible

class ReservasChivas(models.Model):
    destino = models.CharField(max_length=30) #Destino programado para la reserva
    fecha_contratada = models.CharField(max_length=20) #Fecha y hora en la que debe devolver la chiva
    fecha_contratada_hasta = models.CharField(max_length=20)
    chiva_asignada = models.CharField(max_length=20) # matricula de chiva reservada
    nombre_titular = models.CharField(max_length=30)
    identificacion_titular = models.CharField(max_length=15)
    email_titular = models.CharField(max_length=20)
    celular_titular = models.CharField(max_length=10)
    direccion_titular = models.CharField(max_length=30)
    productos_adicionales = models.CharField(max_length=50) #Descripcion de minibar, si no desea adicionar = 0