from django.contrib import admin
from Modulos.Administrador.models import Funcionario, Cargos,Lugar_de_trabajo	

# Register your models here.

admin.site.register(Funcionario)
admin.site.register(Cargos)
admin.site.register(Lugar_de_trabajo)