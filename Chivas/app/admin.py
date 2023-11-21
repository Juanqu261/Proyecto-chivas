from django.contrib import admin
from .models import Viajes, Reservas, Chivas, ReservasChivas, Cancelaciones

# Register your models here.
admin.site.register(Viajes)
admin.site.register(Reservas)
admin.site.register(Chivas)
admin.site.register(ReservasChivas)
admin.site.register(Cancelaciones)