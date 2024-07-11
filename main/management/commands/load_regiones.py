import csv
from django.core.management.base import BaseCommand
from main.models import Region

class Command(BaseCommand):
  def handle(self, *args, **kwargs):
    archivo = open('data/comunas.csv', 'r', encoding='utf-8')
    reader = csv.reader(archivo, delimiter=';')
    next(reader)

    nombres_regiones = []

    for fila in reader:
      if fila[2] not in nombres_regiones:
        #! Si no tenemos el nombre de la region en la lista la agregamos a la base de datos y ademas guardamos su nombre.
        Region.objects.create(nombre=fila[2], cod=fila[3])
        nombres_regiones.append(fila[2])