from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator

# Create your models here.

class PerfilUsuario(models.Model):
  # User:  username(rut), email, fist_name, last_name, password
  user = models.OneToOneField(User, related_name='perfil_usuario', on_delete=models.CASCADE)
  direccion = models.CharField(max_length=255, null= False)
  telefono = models.CharField(max_length=9, null=True)

#! Esto ya lo tiene el "User"
  # nombre = models.CharField(max_length= 50, null=False)
  # apellido = models.CharField(max_length= 50, null=False)
  # rut = models.CharField(max_length=9, primary_key=True, unique=True, null= False)
  # correo = models.CharField(max_length=80, null= False)

#! Esto lo vamos a crear en un grupo despues
  # tipos_usuario = (('arrendatario'), ('arrendador'))
  # tipo_usuario = models.CharField(max_length=12, choices=tipos_usuario)


class Region(models.Model):
  cod = models.CharField(max_length=2, primary_key=True)
  nombre = models.CharField(max_length=255)


class Comuna(models.Model):
  cod = models.CharField(max_length=5, primary_key=True)
  nombre = models.CharField(max_length=255)
  region = models.ForeignKey(Region, on_delete=models.RESTRICT, related_name='comunas')
  
class Inmueble(models.Model):
  nombre = models.CharField(max_length=50)
  descripcion = models.TextField(max_length=1500)
  m2_construidos = models.IntegerField(validators=[MinValueValidator(1)])
  m2_totales = models.IntegerField(validators=[MinValueValidator(1)])
  estacionamientos = models.IntegerField(validators=[MinValueValidator(0)], default=0)
  habitaciones = models.IntegerField(validators=[MinValueValidator(1)], default=1)
  baños = models.IntegerField(validators=[MinValueValidator(0)], default=0)
  direccion = models.CharField(max_length=255)

  tipos_inmueble = (('casa', 'Casa'), ('departamento', 'Deparatamento'), ('parcela', 'Parcela'))
  tipo_de_inmueble = models.CharField(max_length=255, choices=tipos_inmueble)

  precio_mensual_arriendo = models.IntegerField(validators=[MinValueValidator(1000)], null=True)

  #! Llaves foraneas
  comuna = models.ForeignKey(Comuna, related_name='inmuebles', on_delete=models.RESTRICT)
  propietario = models.ForeignKey(User, on_delete=models.RESTRICT, related_name='inmuebles')

class Solicitud(models.Model):
  inmueble = models.ForeignKey(Inmueble, on_delete=models.CASCADE, related_name='solicitudes')
  arrendador = models.ForeignKey(User, related_name='solicitudes', on_delete=models.CASCADE)
  fecha = models.DateTimeField(auto_now_add=True)

  estados = (('pendiente', 'Pendiente'), ('rechazada', 'Rechazada'), ('aprobada', 'Aprobada'))
  estado = models.CharField(max_length=50, choices=estados)