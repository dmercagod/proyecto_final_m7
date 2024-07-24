from main.models import Inmueble, PerfilUsuario, Comuna
from django.contrib.auth.models import User
from django.db.utils import IntegrityError
from django.db.models import Q
from django.db import connection
from django.contrib import messages
from django.shortcuts import render, redirect




# def crear_inmueble(nombre, descripcion, m2_construidos, m2_totales, estacionamientos, habitaciones, baños, direccion, tipo_inmueble, precio_mensual_arriendo, comuna_cod, propietario_rut):

#   comuna = Comuna.objects.get(cod=comuna_cod)

#   propietario = User.objects.get(username=propietario_rut)

#   Inmueble.objects.create(nombre = nombre, 
#     descripcion = descripcion,
#     m2_construidos = m2_construidos,
#     m2_totales = m2_totales,
#     estacionamientos = estacionamientos,
#     habitaciones = habitaciones,
#     baños = baños,
#     direccion = direccion,
#     tipo_de_inmueble = tipo_inmueble,
#     precio_mensual_arriendo = precio_mensual_arriendo,
#     comuna = comuna,
#     propietario = propietario)

def crear_inmueble(nombre, descripcion, m2_construidos, m2_totales, estacionamientos, habitaciones, baños, direccion, tipo_de_inmueble, precio_mensual_arriendo, comuna_cod, propietario_rut):

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
    tipo_de_inmueble = tipo_de_inmueble,
    precio_mensual_arriendo = precio_mensual_arriendo,
    comuna = comuna,
    propietario = propietario)

# def editar_inmueble(nombre, descripcion, m2_construidos, m2_totales, estacionamientos, habitaciones, baños, direccion, tipo_de_inmueble, precio_mensual_arriendo, inmueble_id, cod_comuna, rut):
#   inmueble = Inmueble.objects.get(id=inmueble_id)
#   comuna = Comuna.objects.get(nombre=cod_comuna)
#   propietario = User.objects.get(username=rut)

#   inmueble.nombre = nombre
#   inmueble.descripcion = descripcion
#   inmueble.m2_construidos = m2_construidos
#   inmueble.m2_totales = m2_totales
#   inmueble.estacionamientos = estacionamientos
#   inmueble.habitaciones = habitaciones
#   inmueble.baños = baños
#   inmueble.direccion = direccion
#   inmueble.tipo_de_inmueble = tipo_de_inmueble
#   inmueble.precio_mensual_arriendo = precio_mensual_arriendo
#   inmueble.comuna = comuna
#   inmueble.propietario = propietario
#   inmueble.save()


def editar_inmueble(nombre, descripcion, m2_construidos, m2_totales, estacionamientos, habitaciones, baños, direccion, tipo_de_inmueble, precio_mensual_arriendo, inmueble_id, cod_comuna, rut):
  inmueble = Inmueble.objects.get(id=inmueble_id)
  comuna = Comuna.objects.get(cod=cod_comuna)
  propietario = User.objects.get(username=rut)

  inmueble.nombre = nombre
  inmueble.descripcion = descripcion
  inmueble.m2_construidos = m2_construidos
  inmueble.m2_totales = m2_totales
  inmueble.estacionamientos = estacionamientos
  inmueble.habitaciones = habitaciones
  inmueble.baños = baños
  inmueble.direccion = direccion
  inmueble.tipo_de_inmueble = tipo_de_inmueble
  inmueble.precio_mensual_arriendo = precio_mensual_arriendo
  inmueble.comuna = comuna
  inmueble.propietario = propietario
  inmueble.save()




def eliminar_inmueble(inmueble_id):
  i = Inmueble.objects.get(id=inmueble_id).delete()





def obtener_inmuebles_comunas(filtro):
  if filtro is None:
    return Inmueble.objects.all().order_by('comuna')
  
  #! select * from main_inmueble where nombre like %Elegante% or descripcion like %Elegante%;
  return Inmueble.objects.filter(Q(nombre__icontains=filtro) | Q(descripcion__icontains=filtro)).order_by('comuna')


def obtener_inmuebles_region(filtro):
  if filtro is None:
    return Inmueble.objects.all().order_by('comuna')
  
  return Inmueble.objects.filter(Q(nombre__icontains=filtro) | Q(descripcion__icontains=filtro)).order_by('comuna')


def obtener_inmuebles_region(filtro):
  consulta = '''
    select I.nombre, I.descripcion, R.nombre as region from main_inmueble as I
    join main_comuna as C on I.comuna_id = C.cod
    join main_region as R on C.region_id = R.cod
    order by R.cod;
  '''
  cursor = connection.cursor()
  cursor.execute(consulta)
  registros = cursor.fetchall() # LAZY LOADING
  return registros




def crear_usuario(username, first_name, last_name, email, password, password_confirm, direccion, telefono = None) -> bool:
  
  #! 1. Validamos que ambas contraseñas ingresadas sean iguales
  if password != password_confirm:
    print('constreñas direfrentes')
    return False, 'Las contraseñas no coinciden'
  
  #! 2. Creamos el objeto usuario
  try:
    user = User.objects.create_user(username, email, password, first_name = first_name, last_name=last_name)
    #user.save()
  except IntegrityError:
    return False, 'Rut duplicado'
    


  #! 3. Creamos el perfil de usuario (el create ya viene con un save implicito por lo que no hay que hacer el .save())
  PerfilUsuario.objects.create(user=user, direccion=direccion, telefono=telefono)

  #! 4. Si todo sale bien retornamos true
  return True, None


def registro_usuario(request, username, first_name, last_name, email, password, password_confirm, direccion, rol, telefono = None):
  
  #! 1. Validamos que ambas contraseñas ingresadas sean iguales
  if password != password_confirm:
    messages.info(request, 'Las contraseñas no coinciden, intente nuevamente')
    return
  
  #! 2. Creamos el objeto usuario
  try:
    user = User.objects.create_user(username, first_name = first_name, last_name=last_name, email=email, password=password )
    #user.save()
  except IntegrityError:
    messages.info(request, 'El rut ya existe. Inicie sesión')
    return False, 'Rut duplicado'
    

  telefono = telefono.strip() if telefono and telefono.strip() else None

  #! 3. Creamos el perfil de usuario (el create ya viene con un save implicito por lo que no hay que hacer el .save())
  PerfilUsuario.objects.create(user=user, direccion=direccion, rol=rol, telefono=telefono)
  

  #! 4. Si todo sale bien retornamos true
  messages.success(request, 'El usuario se ha creado correctamente')  
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

def editar_usuario_sin_password(username, first_name, last_name, email, direccion, rol, telefono=None):
  # 1. Nos traemos el 'user' y modificamos sus datos
  user = User.objects.get(username=username)
  user.first_name = first_name
  user.last_name = last_name
  user.email = email
  user.save()
  # 2. Nos traemos el 'user_profile' y modificamos sus datos
  user_profile = PerfilUsuario.objects.get(user=user)
  user_profile.direccion = direccion
  user_profile.rol = rol
  user_profile.telefono = telefono
  user_profile.save()


def cambio_contraseña(request, password, pass_repeat):
  if password != pass_repeat:
    messages.info(request, 'Las contraseñas no coinciden')
    return
  
  request.user.set_password(password)
  request.user.save()
  messages.success(request, 'Se ha actualizado la contraseña correctamente')  
  
  




def eliminar_usuario(rut):
  u = User.objects.get(username = rut)
  u.delete()

