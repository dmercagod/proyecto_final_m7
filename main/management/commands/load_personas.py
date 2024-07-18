import csv
from django.core.management.base import BaseCommand
from main.services import crear_usuario

class Command(BaseCommand):
  def handle(self, *args, **kwargs):
    archivo = open('data/usuarios.csv', 'r', encoding='utf-8')
    reader = csv.reader(archivo, delimiter=';')
    next(reader)

    rut_personas = []

    for fila in reader:
      if fila[11] not in rut_personas:
        #! Si no tenemos el rut de la persona en la lista la agregamos a la base de datos y ademas guardamos su rut.
        crear_usuario(fila[0], fila[1], fila[2], fila[3], fila[4], fila[5], fila[6])
        rut_personas.append(fila[0])