from django.contrib.auth.models import User
from django.db import models


class Fruta(models.Model):
    nombre = models.CharField(max_length=30)
    puntos_salud = models.IntegerField(default=0)

    def __str__(self):
        return self.nombre


class Especie(models.Model):
    nombre = models.CharField(max_length=30)
    fruta_favorita = models.ForeignKey(Fruta, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.nombre


class Humano(models.Model):
    # En general usaríamos models.CASCADE, pero lo dejaremos así para no botar lo que tenemos hasta ahora
    usuario = models.OneToOneField(User, models.SET_NULL, null=True)
    nombre = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre


class Animal(models.Model):
    especie = models.ForeignKey(Especie, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=30)
    salud = models.IntegerField('Puntos de salud', default=0)
    humano = models.ForeignKey(Humano, on_delete=models.SET_NULL, blank=True, null=True)
    imagen = models.ImageField(upload_to='fotitos', default='fotitos/sin_fotito.jpg')

    def __str__(self):
        return '%s (%s)' % (self.nombre, self.especie.nombre)

    class Meta:
        verbose_name_plural = "Animales"

