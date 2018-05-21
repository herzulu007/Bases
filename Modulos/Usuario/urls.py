from django.urls import path
from Modulos.Usuario.views import Pagina_principal_usuario, Usuario_view


urlpatterns = [
    path('', Pagina_principal_usuario, name='index'),
    path('nuevo/', Usuario_view,name='Crear_usuario' ),
]
