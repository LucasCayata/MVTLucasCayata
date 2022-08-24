from django.http import HttpResponse
from django.shortcuts import render
from .models import Familiar
from django.template import Context, Template, loader

# Create your views here.

def familiar(request):
    familiar1=Familiar(nombre="Lujan Perez",dni=34037282,fecha_nacimiento="1990-07-13")
    familiar1.save()
    familiar2=Familiar(nombre="Jose Perez",dni=12169919,fecha_nacimiento="1956-09-19")
    familiar2.save()
    familiar3=Familiar(nombre="Mirta Gonzalez",dni=14607662,fecha_nacimiento="1959-04-13")
    familiar3.save()
    lista_familiares=[familiar1,familiar2,familiar3]
    diccionario={"familiar1":lista_familiares[0], "familiar2":lista_familiares[1],"familiar3":lista_familiares[2]}
    plantilla=loader.get_template("template.html")
    documento=plantilla.render(diccionario)
    return HttpResponse(documento)

