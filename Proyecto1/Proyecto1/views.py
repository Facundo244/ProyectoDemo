from datetime import datetime
from django.http import HttpResponse 
import datetime
from django.template  import Template , Context
from django.template import loader


def saludo(request):
    return HttpResponse("Hola mundo")

def segunda_vista(request):
    return HttpResponse("Segunda Vista")

def DiaDeHoy(request):
    dia = datetime.datetime.now()
    texto = 'Hoy es: {}'.format(dia)
    return HttpResponse(texto)


def nombre_persona(self,nombre):
    resultado = "Mi nombre es: <br> <br> {}".format(nombre)
    return HttpResponse(resultado)


def probandoTemplate(self):

    nombre = 'Bruno'
    apellido = 'Arias'
    listaDeNotas = [2,5,7,3]

    diccionario = {"nombre":nombre,"apellido":apellido,"listaDeNotas":listaDeNotas}

    #miHtml = open("template1.html")

    #plantilla = Template(miHtml.read()) #Se carga en memoria nuestro documento, template1   
    ##OJO importar template y contex, con: from django.template import Template, Context

    #miHtml.close() #Cerramos el archivo

    #miContexto = Context(diccionario) #EN este caso no hay nada ya que no hay parametros, IGUAL hay que crearlo
    plantilla = loader.get_template('template1.html')
    documento = plantilla.render(diccionario) #Aca renderizamos la plantilla en documento

    return HttpResponse(documento)