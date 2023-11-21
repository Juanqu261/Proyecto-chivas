from django.urls import path
from app import views

urlpatterns = [
    path('',views.index,name="index2"),
    path('comprarTiquete/<int:viaje_id>/',views.comprarTiquete, name="comprarTiquete"),
    path('cantidadTiquetes/', views.cantidadTiquetes, name='cantidadTiquetes'),
    path('reservar/<int:viaje_id>/', views.reservar, name="reservar"),
    path('seleccionarChiva/', views.seleccionarChiva, name='seleccionarChiva'),
    path('cancelaciones/',views.cancelaciones,name='cancelaciones'),
    path('reservarChiva/',views.reservarChiva,name='reservarChiva'),
    path('buscarReserva/',views.buscarReserva,name='buscarReserva'),
    path('cancelarReserva/<int:reserva_id>/',views.cancelarReserva,name='cancelarReserva'),
]
