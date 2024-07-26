from django.urls import path, include
from main.views import *

urlpatterns = [
  path('accounts/', include('django.contrib.auth.urls')),
  path('', index, name = 'index'),
  path('accounts/profile/', perfil, name = 'perfil'),
  path('accounts/register/', register, name = 'register'),
  path('editar-usuario/', editar_usuario, name = 'editar-usuario'),
  path('registrar-usuario/', registrar_usuario, name = 'registrar-usuario'),
  path('accounts/cambiar-contraseña/', cambiar_contraseña, name = 'cambiar-contraseña'),
  path('inmuebles/', inmuebles, name = 'inmuebles'),

  path('publicar-inmueble/', publicar_inmueble, name = 'publicar-inmueble'),
  path('crear-inmuebles/', crear_inmuebles, name = 'crear-inmuebles'),
  path('inmueble/editar/<id>/', editar_inmueble_creado, name = 'editar-inmueble'),
  path('inmueble/ver/', ver_inmuebles_creados, name = 'ver-inmuebles'),
  path('inmueble/eliminar/<id>', eliminar_inmueble_creado, name = 'eliminar-inmueble'),

  
  
  
]
