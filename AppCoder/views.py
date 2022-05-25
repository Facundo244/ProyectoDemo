from django.http import HttpResponse
from django.shortcuts import render
from AppCoder import views

from AppCoder.models import Curso

def curso(self):
    curso = Curso(nombre= "Desarrolo backend" , camada =18340)
    curso.save
    documento = f"Curso: {curso.nombre} - Camada: {curso.camada}"
    return HttpResponse(documento)


def profesores(self):
    documento = f"Pagina de profesores"
    return HttpResponse(documento)
