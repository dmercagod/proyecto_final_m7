from django.contrib import admin
from main.models import Comuna, Inmueble, PerfilUsuario 
# Register your models here.


class ComunaAdmin(admin.ModelAdmin):
  pass

admin.site.register(Comuna, ComunaAdmin)

class InmuebleAdmin(admin.ModelAdmin):
  pass

admin.site.register(Inmueble, InmuebleAdmin)

class PerfilUsuarioAdmin(admin.ModelAdmin):
  pass

admin.site.register(PerfilUsuario, PerfilUsuarioAdmin)