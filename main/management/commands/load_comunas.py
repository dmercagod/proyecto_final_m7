import csv
from django.core.management.base import BaseCommand
from main.models import Comuna

class Command(BaseCommand):
  def handle(self, *args, **kwargs):
    archivo = open('data/comunas.csv', 'r', encoding='utf-8')
    reader = csv.reader(archivo, delimiter=';')
    next(reader)
    next(reader)
    nombres_comunas = []
    for fila in reader:
      if fila[2] not in nombres_comunas:
        #! Si no tenemos el nombre de la region en la lista la agregamos a la base de datos y ademas guardamos su nombre.
        Comuna.objects.create(nombre=fila[0], cod=fila[1], region_id=fila[3])

      