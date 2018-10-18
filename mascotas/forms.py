from django import forms


class AgregarFotoMascota(forms.Form):
    imagen = forms.ImageField()
