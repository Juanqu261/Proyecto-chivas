from django.shortcuts import render, get_object_or_404
from .models import Viajes

# Create your views here.
def index(request):
    viajes = Viajes.objects.all()
    return render(request, 'index2.html', {'viajes': viajes})

def comprarTiquete(request, viaje_id):
    viaje = get_object_or_404(Viajes, id=viaje_id)
    return render(request, 'comprarTiquete.html', {'viaje': viaje})

def cantidadTiquetes(request):
    viaje_id = request.POST.get('viaje_id')  
    viaje = get_object_or_404(Viajes, pk=viaje_id)
    if request.method == 'POST':
        selected_value = request.POST.get('selectField', None)
        return render(request, 'comprarTiquete.html', {'selected_value': selected_value, 'viaje':viaje})
    return render(request, 'comprarTiquete.html', {'selected_value': None})
