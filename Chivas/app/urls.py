from django.urls import path
from app import views

urlpatterns = [
    path('',views.index,name="index2"),
    path('comprarTiquete/<int:viaje_id>/',views.comprarTiquete, name="comprarTiquete"),
    path('cantidadTiquetes/', views.cantidadTiquetes, name='cantidadTiquetes'),
]
