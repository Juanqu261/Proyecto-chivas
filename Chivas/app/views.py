from django.shortcuts import render
from .models import Viajes

# Create your views here.
def index(request):
    return render(request, "index2.html", {
        'viajes' : Viajes.objects.all()
    })