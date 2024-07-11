from main.services import *
from django.core.management.base import BaseCommand

class Command(BaseCommand):
  def handle(self, *args, **kwargs):

    crear_usuario('11111111-1', 'Jhon', 'Doe', 'jhondoe@mail.cl', '1234', '1234', 'av. avenida 1')
    # crear_usuario('1231231-4', 'Jhon', 'Doe', 'jhondoe@mail.cl', '1234', '1234', 'av. avenida 1')



    # editar_usuario('3333333-3', 'Jhon', 'Doe', 'jhondoe@mail.cl', '12345', 'av. avenida 333')

    # crear_inmueble('casita', 'casa cuadrada', 120, 250, 1, 1, 1, 'av. avenida 1', 'casa', 500_000, '05606', 11111111-1)