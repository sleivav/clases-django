from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from mascotas.models import Animal


def index(request):
    animales = Animal.objects.all()
    return render(request, 'mascotas/index.html', {'animales': animales})


def humano(request, humano):
    animales = Animal.objects.filter(humano_id=humano)
    return render(request, 'mascotas/index.html', {'animales': animales})


# Esta función fue creada temporalmente para que la app corra
def subir_foto(request):
    return None


def detalles_animal(request, mascota):
    animal = Animal.objects.get(id=mascota)
    return render(request, 'mascotas/detalles_mascota.html', {'mascota': animal})
