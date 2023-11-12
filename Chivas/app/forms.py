from django import forms
from .models import Reservas

class ReservasForm(forms.ModelForm):
    class Meta:
        model = Reservas
        fields = ['viaje_reservado', 'asientos_reservados', 'nombre_titular', 'identificacion_titular', 
                  'email_titular', 'celular_titular', 'direccion_titular']
        labels = {
            'viaje_reservado':'Viaje Reservado', 
            'asientos_reservados': "Asientos Reservados", 
            'nombre_titular':"Nombre", 
            'identificacion_titular':"Identificacion", 
            'email_titular':"Email", 
            'celular_titular':"Celular", 
            'direccion_titular':"Direccion"
        }
        
        widgets = {
            'viaje_reservado':forms.TextInput(attrs={'class': 'form-control'}), 
            'asientos_reservados': forms.TextInput(attrs={'class': 'form-control'}), 
            'nombre_titular':forms.TextInput(attrs={'class': 'form-control'}), 
            'identificacion_titular':forms.TextInput(attrs={'class': 'form-control'}), 
            'email_titular':forms.TextInput(attrs={'class': 'form-control'}), 
            'celular_titular':forms.TextInput(attrs={'class': 'form-control'}), 
            'direccion_titular':forms.TextInput(attrs={'class': 'form-control'})
        }