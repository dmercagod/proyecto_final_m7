from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test

from main.services import *
from main.models import *
from main.forms import *

#! Filtro para que solo pasen los arrendadores
def solo_arrendadores(user):
  if user.perfil_usuario.rol == 'arrendador' or user.is_staff == True:
    return True
  else:
    return False


# Create your views here.

def index(request):

  
  inmuebles = Inmueble.objects.all()
  context = {
    'inmuebles':inmuebles
  }
  return render(request, 'index.html', context)



@login_required
def perfil(request):
  return render(request, 'perfil.html')
  

@login_required
def editar_usuario(request):
    # 1. Obtengo el usuario actual
  current_user = request.user
  # llamo a la función para editar el usuario
  if request.POST['telefono'].strip() != '':
    # trailing whitespaces .strip()
    editar_usuario_sin_password(
      current_user.username,
      request.POST['first_name'],
      request.POST['last_name'],
      request.POST['email'],
      request.POST['direccion'],
      request.POST['rol'],
      request.POST['telefono'])
  else:
    editar_usuario_sin_password(
      current_user.username,
      request.POST['first_name'],
      request.POST['last_name'],
      request.POST['email'],
      request.POST['direccion'],
      request.POST['rol'])
      
  
  messages.success(request, "Se han actualizado los datos correctamente")
  return redirect('perfil')
  

@login_required
def cambiar_contraseña(request):
  #! 1. Recibo los datos del formulario
  password = request.POST['password']
  pass_repeat = request.POST['pass_repeat']

  #! 2. Valido que ambas contraseñas coincidan
  # if password != pass_repeat:
  #   messages.info(request, 'Las contraseñas no coinciden')
  #   return redirect('/accounts/profile')
  
  # #! 3. Actualizamos la contraseña
  # request.user.set_password(password)
  # request.user.save()

  # #! 4. Le avisamos al usuario que el cambio fue exitoso
  # messages.success(request, 'Se ha actualizado la contraseña correctamente')

  cambio_contraseña(request, password, pass_repeat)

  return redirect('perfil')



def register(request):
  return render(request, 'register.html')


def registrar_usuario(request):
  username = request.POST['username']
  first_name = request.POST['first_name']
  last_name = request.POST['last_name']
  email = request.POST['email']
  password = request.POST['password']
  password_confirm = request.POST['password_confirm']
  direccion = request.POST['direccion']
  rol = request.POST['rol']
  telefono = request.POST['telefono']
  

  registro_usuario(request, username, first_name, last_name, email, password, password_confirm, direccion, rol, telefono)

  return redirect('register')



def inmuebles(request):

  
  datos = request.GET
  region_cod = datos.get('region_cod', '')
  comuna_cod = datos.get('comuna_cod', '')
  palabra = datos.get('palabra', '')
  tipo = datos.get('tipo_de_inmueble', '')
  

  inmuebles = filtro_inmuebles(region_cod, comuna_cod, palabra, tipo)

  regiones = Region.objects.all()
  comunas = Comuna.objects.all()

  context = {
    'inmuebles': inmuebles,
    'comunas': comunas,
    'regiones': regiones,
    'tipos_inmueble': Inmueble.tipos_inmueble
    }

  return render(request,'inmuebles.html', context)









@user_passes_test(solo_arrendadores)
def publicar_inmueble(request):
  #! Nos traemos la informacion de las comunas y las regiones
  regiones = Region.objects.all()
  comunas = Comuna.objects.all()
  #! Pasar los datos requeridos por el formulario
  
  context = {
    'tipos_inmueble': Inmueble.tipos_inmueble,
    'regiones': regiones,
    'comunas': comunas
  }
  return render(request, 'publicar.html', context)

@user_passes_test(solo_arrendadores)
def crear_inmuebles(request):

  nombre = request.POST['nombre'] 
  descripcion = request.POST['descripcion'] 
  m2_construidos = int(request.POST['m2_construidos'])
  m2_totales = int(request.POST['m2_totales'])
  estacionamientos = int(request.POST['estacionamientos'])
  habitaciones = int(request.POST['habitaciones'])
  baños = int(request.POST['baños'])
  direccion = request.POST['direccion']
  tipo_de_inmueble = request.POST['tipo_de_inmueble']  
  precio_mensual_arriendo = int(request.POST['precio_mensual_arriendo'])
  imagen_ruta = request.POST['imagen_ruta']
  comuna_cod = request.POST['comuna_cod']
  propietario_rut = request.user.username
    
  crear_inmueble(nombre, descripcion, m2_construidos, m2_totales, estacionamientos, habitaciones, baños, direccion, tipo_de_inmueble, precio_mensual_arriendo, imagen_ruta, comuna_cod, propietario_rut)

  messages.success(request, "El inmueble se publicó correctamente")
  return redirect('publicar-inmueble')




@user_passes_test(solo_arrendadores)
def editar_inmueble_creado(request, id):

  if request.method == 'GET':

    inmueble = Inmueble.objects.get(id=id)
    regiones = Region.objects.all()
    comunas = Comuna.objects.all()
    cod_region = inmueble.comuna_id[0:2]

    context = {
      'inmueble':inmueble,
      'regiones': regiones,
      'comunas': comunas,
      'cod_region': cod_region
    }

    return render(request, 'editar_inmueble.html', context)
  
  else:
      
      rut = request.user.username

      editar_inmueble(
        id,
        request.POST['nombre'],
        request.POST['descripcion'],
        int(request.POST['m2_construidos']),
        int(request.POST['m2_totales']),
        int(request.POST['estacionamientos']),
        int(request.POST['habitaciones']),
        int(request.POST['baños']),
        request.POST['direccion'],
        request.POST['tipo_de_inmueble'],
        int(request.POST['precio_mensual_arriendo']),
        request.POST['imagen_ruta'],
        request.POST['comuna_cod'],
        rut
      )

      messages.success(request, "El inmueble se modificó correctamente")
      return redirect('editar-inmueble', id= id)







@user_passes_test(solo_arrendadores)
def eliminar_inmueble_creado(request, id):
    print('eliminando ' + id)

    eliminar_inmueble(id)
    messages.success(request, "El inmueble se eliminó correctamente")
    return redirect('/inmueble/ver/')









@user_passes_test(solo_arrendadores)
def ver_inmuebles_creados(request):
  current_user = request.user
  inmuebles = None

  if current_user.perfil_usuario.rol == 'arrendador':
    inmuebles = current_user.inmuebles.all()
  elif current_user.perfil_usuario.rol == 'arrendatario':
    pass

  
  context = {
    'inmuebles':inmuebles
  }

  return render(request, 'ver_inmuebles_creados.html', context)





