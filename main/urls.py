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
  path('inmuebles/<tipo_de_inmueble>/', inmuebles, name = 'inmuebles'),
  path('regiones/<comuna_id>/', filtro_ciudades, name = 'filtro_ciudades'),
  path('publicar-inmueble/', publicar_inmueble, name = 'publicar-inmueble'),
  path('crear-inmuebles/', crear_inmuebles, name = 'crear-inmuebles/'),
  
  
  
]
