from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from mascotas.forms import AgregarFotoMascota
from mascotas.models import Animal


def index(request):
    animales = Animal.objects.all()
    return render(request, 'mascotas/index.html', {'animales': animales})


def humano(request, humano):
    animales = Animal.objects.filter(humano_id=humano)
    return render(request, 'mascotas/index.html', {'animales': animales})


def subir_foto(request, animal):
    animal = Animal.objects.get(id=animal)
    if request.method == 'POST':
        form = AgregarFotoMascota(request.POST, request.FILES)
        if form.is_valid():
            animal.imagen = form.cleaned_data['imagen']
            animal.save()
    return redirect('detalles_animal', mascota=animal.id)


def detalles_animal(request, mascota):
    animal = Animal.objects.get(id=mascota)
    return render(request, 'mascotas/detalles_mascota.html', {'mascota': animal})
