from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib import messages

from main.services import *
from main.models import *


# Create your views here.

def index(request):
  # casas = Inmueble.objects.filter(tipo_de_inmueble__iexact='casa')
  # context = {
  #   'casas': casas
  #   }
  inmuebles = Inmueble.objects.all()
  context = {
    'inmuebles':inmuebles
  }
  return render(request, 'index.html', context)

# @login_required
# def perfil(request):
#   return render(request, 'perfil.html')

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
      request.POST['telefono'])
  else:
    editar_usuario_sin_password(
      current_user.username,
      request.POST['first_name'],
      request.POST['last_name'],
      request.POST['email'],
      request.POST['direccion'])
  
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



def registro(request):
  return render(request, 'registro.html')


def solo_arrendadores(req):
  return HttpResponse('solo arrendadores')

def solo_arrendatarios(req):
  return HttpResponse('solo arrendatarios')