from django.http import HttpResponse
from django.shortcuts import render
from clase.models import Curso
import random

# Create your views here.

def nuevo_curso(request):
    comision = random.randrange(1500, 3000)
    nuevo_curso = Curso(nombre='Curso Python', comision=comision)
    nuevo_curso.save()
    return HttpResponse(f'Se creo el curso {nuevo_curso.nombre} comision {nuevo_curso.comision}')