
from curses.ascii import HT
from re import A
from django.http import HttpResponse
import random
from django.shortcuts import render

from django.template import Context, Template, loader  #Context y Template, con la segunda forma noson necesarios.


def inicio(request):
    return render(request, 'indice/index.html', {})

def otra_vista(request):
    return HttpResponse('''
                        <h1>Este es un título
                        en h1</h1>''')
    
def numero_random(request):
    numero = random.randrange(15, 200)
    texto = f'<h1>Este es tu numero random: {numero}</h1>'
    return HttpResponse(texto)

def numero_del_usuario(request, numero):
    texto = f'<h1>Este es tu numero: {numero}</h1>'
    return HttpResponse(texto)

def edad_usuario(request, numero):
    año_nacimiento = 2022 - numero
    return HttpResponse(año_nacimiento)

def mi_plantilla(request):
    nombre = 'Jorge'
    apellido = 'Atahualpa'
    lista = [34,5,6,12,9,43,3]
    diccionario_de_datos = {
        'nombre': nombre,
        'apellido': apellido,
        'nombre_largo': len(nombre),
        'lista': lista
    }
    
    # version vieja con open 
    # plantilla = open(r'C:\Users\pablo\OneDrive\Documentos\MIPROYECTO\miproyecto\plantillas\mi_plantilla.html')
    # template = Template(plantilla.read())
    # context = Context(diccionario_de_datos)
    # plantilla.close(r'C:\Users\pablo\OneDrive\Documentos\MIPROYECTO\miproyecto\plantillas\mi_plantilla.html')
   
    #version nueva con loader(hay otra version mas resumida que vamos a ver mas adelante)
    # template = loader.get_template('mi_plantilla.html') #esta línea reemplaza las 4 de arriba
    # plantilla_preparada = template.render(diccionario_de_datos)
   
    # return HttpResponse(plantilla_preparada)
    
    # Version con render
    return render(request, 'indice/mi_plantilla.html', diccionario_de_datos)