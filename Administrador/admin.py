from django.contrib import admin
from Modulos.Administrador.models import Cede,Funcionario,Cargos,Lugar,Tipo_solicitud,Solicitud,Entidad_receptora,Entidad_emisora

# Register your models here.

admin.site.register(Funcionario)
admin.site.register(Cargos)
admin.site.register(Lugar)
admin.site.register(Tipo_solicitud)
admin.site.register(Solicitud)
admin.site.register(Entidad_emisora)
admin.site.register(Entidad_receptora)
admin.site.register(Cede)