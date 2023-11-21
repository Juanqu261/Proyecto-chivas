from django.shortcuts import render, get_object_or_404
from .models import Viajes, Reservas, Chivas, ReservasChivas, Cancelaciones
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

def seleccionarChiva(request):
    chivas = Chivas.objects.filter(estado=1)

    if chivas.exists():
        chiva_disponible = choice(chivas)
        form = ReservarChivaForm()
        form.fields['chiva_asignada'].initial = chiva_disponible.matricula
        form.fields['productos_adicionales'].initial = 0
        return render(request, 'reservarChiva.html', {'form':form, 'chiva_disponible':chiva_disponible})
    else:
        return render(request, 'reservarChiva.html', {'chivas':chivas, 'chiva_disponible':None})
    
def reservarChiva(request):
    if request.method == 'POST':
        form = ReservarChivaForm(request.POST)
        if form.is_valid():
            new_destino = form.cleaned_data["destino"]
            new_fecha_contratada = form.cleaned_data["fecha_contratada"]
            new_fecha_contratada_hasta = form.cleaned_data["fecha_contratada_hasta"]
            new_chiva_asignada = form.cleaned_data["chiva_asignada"]
            new_nombre_titular = form.cleaned_data["nombre_titular"]
            new_identificacion_titular = form.cleaned_data["identificacion_titular"]
            new_email_titular = form.cleaned_data["email_titular"]
            new_celular_titular = form.cleaned_data["celular_titular"]
            new_direccion_titular = form.cleaned_data["direccion_titular"]
            new_productos_adicionales = form.cleaned_data["productos_adicionales"]
            new_reserva_chiva = ReservasChivas(
                destino=new_destino,
                fecha_contratada=new_fecha_contratada,
                fecha_contratada_hasta=new_fecha_contratada_hasta,
                chiva_asignada=new_chiva_asignada,
                nombre_titular=new_nombre_titular,
                identificacion_titular=new_identificacion_titular,
                email_titular=new_email_titular,
                celular_titular=new_celular_titular,
                direccion_titular=new_direccion_titular,
                productos_adicionales=new_productos_adicionales,
            )
            new_reserva_chiva.save()
            matricula = Chivas.objects.get(matricula=new_chiva_asignada)
            matricula.estado = '0'
            matricula.save()
            return render(request, 'reservarChiva.html', {
                'form': form,
                'success' : True,
                'reserva':new_reserva_chiva
            })

def cancelaciones(request):
    return render(request, 'cancelaciones.html')

def buscarReserva(request):
    if request.method == 'POST':
        documento_identidad = request.POST.get('documento_identidad')
        numero_reserva = request.POST.get('numero_reserva')
        tipo_reserva = request.POST.get('tipo_reserva')
        reserva = None
        if tipo_reserva == 'Reserva de viaje':
            
            if Reservas.objects.filter(id=numero_reserva).exists():
                reserva = Reservas.objects.get(id=numero_reserva)
                viaje = Viajes.objects.get(id=reserva.viaje_reservado)
                if reserva.identificacion_titular != documento_identidad:
                    reserva = None
            else:
                reserva = None
        if tipo_reserva == 'Reserva de chiva':
            viaje = None
            if ReservasChivas.objects.filter(id=numero_reserva).exists():
                reserva = ReservasChivas.objects.get(id=numero_reserva)
                if reserva.identificacion_titular != documento_identidad:
                    reserva = None
            else:
                reserva = None
        return render(request, 'cancelaciones.html', {
            'reserva': reserva,
            'viaje':viaje
        })

def cancelarReserva(request, reserva_id):
    if request.method == 'POST':
        if 'reserva_viaje' in request.POST:
            reserva = Reservas.objects.get(id=reserva_id)
            viaje = Viajes.objects.get(id=reserva.viaje_reservado)
            asientos_cancelados = request.POST.get('selectField')
            if int(asientos_cancelados) > int(reserva.asientos_reservados):
                return render(request, 'cancelaciones.html', {'cancelado':False})
            elif int(asientos_cancelados) == int(reserva.asientos_reservados):
                viaje.asientos_disponibles = str(int(viaje.asientos_disponibles)+int(reserva.asientos_reservados))
                cancelacion = Cancelaciones(
                    tipo_reserva='viaje',
                    numero_reserva=reserva_id,
                    asientos_devueltos='-1',
                    nombre_titular=reserva.nombre_titular,
                    identificacion_titular=reserva.identificacion_titular
                )
                cancelacion.save()
                viaje.save()
                reserva.delete()
                return render(request, 'cancelaciones.html', {'cancelado':True, 'cancelacion':cancelacion})
            else:
                reserva.asientos_reservados = str(int(reserva.asientos_reservados)-int(asientos_cancelados))
                viaje.asientos_disponibles = str(int(viaje.asientos_disponibles)+int(asientos_cancelados))
                cancelacion = Cancelaciones(
                    tipo_reserva='viaje',
                    numero_reserva=reserva_id,
                    asientos_devueltos=asientos_cancelados,
                    nombre_titular=reserva.nombre_titular,
                    identificacion_titular=reserva.identificacion_titular
                )
                cancelacion.save()
                reserva.save()
                viaje.save()
                return render(request, 'cancelaciones.html',{'cancelado':True, 'cancelacion':cancelacion})
        if 'reserva_chiva' in request.POST:
            reserva = ReservasChivas.objects.get(id=reserva_id)
            chiva = Chivas.objects.get(matricula=reserva.chiva_asignada)
            chiva.estado = '1'
            cancelacion = Cancelaciones(
                tipo_reserva='chiva',
                numero_reserva=reserva_id,
                asientos_devueltos='-1',
                nombre_titular=reserva.nombre_titular,
                identificacion_titular=reserva.identificacion_titular
                )
            cancelacion.save()
            chiva.save()
            reserva.delete()
            return render(request, 'cancelaciones.html',{'cancelado':True, 'cancelacion':cancelacion})