from django.db import models

# Create your models here.

class Usuario(models.Model):
  nombres = models.CharField(max_length= 50, null=False)
  apellidos = models.CharField(max_length= 50, null=False)
  rut = models.CharField(max_length=9, primary_key=True, unique=True, null= False)
  direccion = models.CharField(max_length=80, null= False)
  telefono = models.IntegerField(max_length=9, null= False)
  correo = models.CharField(max_length=80, null= False)
  tipo_usuario = models.CharField(max_length=12)


class Inmueble(models.Model):
  nombre = models.CharField()
  descripcion = models.CharField()
  m2_construidos = models.IntegerField()
  m2_totales = models.IntegerField()
  estacionamientos = models.IntegerField()
  habitaciones = models.IntegerField()
  baños = models.IntegerField()
  direccion = models.IntegerField()
  comuna = models.CharField()

  tipo_inmueble = ['casa', 'departamento', 'parcela']
  tipo_de_inmueble = models.CharField(choices=tipo_inmueble)

  precio_mensual_arriendo = models.CharField()