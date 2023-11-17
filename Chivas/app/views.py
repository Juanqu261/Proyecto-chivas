from django.shortcuts import render, get_object_or_404
from .models import Viajes, Reservas, Chivas
from .forms import ReservasForm, ReservarChivaForm
from random import choice

# Create your views here.
def index(request):  
    viajes = Viajes.objects.all()
    return render(request, 'index2.html', {'viajes': viajes})

def comprarTiquete(request, viaje_id):

    viaje = get_object_or_404(Viajes, id=viaje_id)
    return render(request, 'comprarTiquete.html', {'viaje': viaje})

def cantidadTiquetes(request):
    form = ReservasForm()
    viaje_id = request.POST.get('viaje_id')  
    viaje = get_object_or_404(Viajes, pk=viaje_id)
    if request.method == 'POST':
        selected_value = request.POST.get('selectField', None)
        form.fields['viaje_reservado'].initial = viaje.id
        form.fields['asientos_reservados'].initial = selected_value
        return render(request, 'comprarTiquete.html', {'selected_value': selected_value, 'viaje':viaje, 'form':form})
    return render(request, 'comprarTiquete.html', {'selected_value': None})

def reservar(request, viaje_id):

    if request.method == 'POST':
        form = ReservasForm(request.POST)
        if form.is_valid():
            new_viaje_reservado = form.cleaned_data["viaje_reservado"]
            new_asientos_reservados = form.cleaned_data["asientos_reservados"]
            new_nombre_titular = form.cleaned_data["nombre_titular"]
            new_identificacion_titular = form.cleaned_data["identificacion_titular"]
            new_email_titular = form.cleaned_data["email_titular"]
            new_celular_titular = form.cleaned_data["celular_titular"]
            new_direccion_titular = form.cleaned_data["direccion_titular"]

            new_reserva = Reservas(
                viaje_reservado = new_viaje_reservado,
                asientos_reservados = new_asientos_reservados,
                nombre_titular = new_nombre_titular,
                identificacion_titular = new_identificacion_titular,
                email_titular = new_email_titular,
                celular_titular = new_celular_titular,
                direccion_titular = new_direccion_titular
            )
            new_reserva.save()
            #Modificar los asientos disponibles del viaje reservado
            viaje = Viajes.objects.get(id=viaje_id)
            viaje.asientos_disponibles = str(int(viaje.asientos_disponibles)-int(new_asientos_reservados))
            viaje.save()
            return render(request, "comprarTiquete.html",{
                'form': form,
                'success' : True,
                'reserva':new_reserva
            })
    else:
        form = ReservasForm()
        return render(request, 'comprarTiquete.html',{
            'form' : form
        })

def reservarChiva(request):
    chivas = Chivas.objects.filter(estado=1)

    if chivas.exists():
        chiva_disponible = choice(chivas)
        form = ReservarChivaForm()
        form.fields['chiva_asignada'].initial = chiva_disponible.matricula
        form.fields['productos_adicionales'].initial = 0
        return render(request, 'reservarChiva.html', {'form':form, 'chiva_disponible':chiva_disponible})
    else:
        return render(request, 'reservarChiva.html', {'chivas':chivas, 'chiva_disponible':None})

def cancelaciones(request):
    return render(request, 'cancelaciones.html')