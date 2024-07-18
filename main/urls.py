from django.urls import path, include
from main.views import *

urlpatterns = [
  path('accounts/', include('django.contrib.auth.urls')),
  path('', index),
  path('accounts/profile/', perfil, name = 'perfil'),
  path('editar-usuario/', editar_usuario, name = 'editar-usuario'),
  path('accounts/cambiar-contraseña/', cambiar_contraseña, name = 'cambiar-contraseña'),
  
  
]
