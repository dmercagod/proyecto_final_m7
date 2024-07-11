from main.models import Inmueble, PerfilUsuario, Comuna
from django.contrib.auth.models import User
from django.db.utils import IntegrityError


def crear_inmueble(nombre, descripcion, m2_construidos, m2_totales, estacionamientos, habitaciones, baños, direccion, tipo_inmueble, precio_mensual_arriendo, comuna_cod, propietario_rut):

  comuna = Comuna.objects.get(cod=comuna_cod)

  propietario = User.objects.get(username=propietario_rut)

  Inmueble.objects.create(nombre = nombre, 
    descripcion = descripcion,
    m2_construidos = m2_construidos,
    m2_totales = m2_totales,
    estacionamientos = estacionamientos,
    habitaciones = habitaciones,
    baños = baños,
    direccion = direccion,
    tipo_inmueble = tipo_inmueble,
    precio_mensual_arriendo = precio_mensual_arriendo,
    comuna = comuna,
    propietario = propietario)


def editar_inmueble(inmueble_id, nombre, descripcion, m2_construidos, m2_totales, estacionamientos, habitaciones, baños, direccion, tipo_inmueble, precio_mensual_arriendo):
  pass


def eliminar_inmueble(inmueble_id):
  i = Inmueble.objects.get(id = inmueble_id)
  i.delete()










def crear_usuario(username, first_name, last_name, email, password, password_confirm, direccion, telefono = None) -> bool:
  print('llegamos')
  #! 1. Validamos que ambas contraseñas ingresadas sean iguales
  if password != password_confirm:
    print('constreñas direfrentes')
    return False, 'Las contraseñas no coinciden'
  #! 2. Creamos el objeto usuario
  try:
    user = User.objects.create_user(username, email, password, first_name = first_name, last_name=last_name)
    #user.save()
  except IntegrityError:
    print('rut duplicados')
    print(username)
    print(email)
    print(password)
    print(first_name)
    print(last_name)
    return False, 'Rut duplicado'
    


  #! 3. Creamos el perfil de usuario (el create ya viene con un save implicito por lo que no hay que hacer el .save())
  PerfilUsuario.objects.create(user=user, direccion=direccion, telefono=telefono)

  #! 4. Si todo sale bien retornamos true
  return True, None


def editar_usuario(user, first_name, last_name, email, password, direccion, telefono = None):
  #! 1. Nos traemos el user y modificamos sus datos
  username = User.objects.get(username = user)
  username.first_name = first_name
  username.last_name = last_name
  username.email = email
  username.set_password(password)
  username.save()

  #! 2. Nos traemos el perfil usuario y modificamos sus datos
  perfil_usuario = PerfilUsuario.objects.get(user= username)
  perfil_usuario.direccion = direccion
  perfil_usuario.telefono = telefono
  perfil_usuario.save()


def eliminar_usuario(user):
  u = PerfilUsuario.objects.get(user = user)
  u.delete()

