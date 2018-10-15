from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name=''),
    path('<int:humano>', views.humano, name='humano'),
    path('/subir_foto/<int: animal>', views.subir_foto, name='subir_foto'),
]