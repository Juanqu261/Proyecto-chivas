from django import forms
from .models import Reservas, ReservasChivas

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

class ReservarChivaForm(forms.ModelForm):
    class Meta:
        model = ReservasChivas
        fields = ['destino','fecha_contratada','fecha_contratada_hasta','chiva_asignada','nombre_titular','identificacion_titular',
                  'email_titular','celular_titular','direccion_titular','productos_adicionales']
        labels = {  'destino':'Destino',
                    'fecha_contratada':'Reservar hasta',
                    'fecha_contratada_hasta':'Contratar hasta',
                    'chiva_asignada':'Matricula de chiva a reservar',
                    'nombre_titular':'Nombre',
                    'identificacion_titular':'Identificacion',
                    'email_titular':"Email", 
                    'celular_titular':"Celular", 
                    'direccion_titular':"Direccion",
                    'productos_adicionales':'Productos adicionales (minibar)'}
        widgets = {
            'destino':forms.TextInput(attrs={'class': 'form-control'}), 
            'fecha_contratada':forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_contratada_hasta':forms.TextInput(attrs={'class': 'form-control'}),
            'chiva_asignada': forms.TextInput(attrs={'class': 'form-control'}), 
            'nombre_titular':forms.TextInput(attrs={'class': 'form-control'}), 
            'identificacion_titular':forms.TextInput(attrs={'class': 'form-control'}), 
            'email_titular':forms.TextInput(attrs={'class': 'form-control'}), 
            'celular_titular':forms.TextInput(attrs={'class': 'form-control'}), 
            'direccion_titular':forms.TextInput(attrs={'class': 'form-control'}),
            'productos_adicionales':forms.Textarea(attrs={'class': 'form-control'})
        }