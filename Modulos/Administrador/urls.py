from django.urls import path
from Modulos.Administrador.views import Pagina_principal


urlpatterns = [
    path('', Pagina_principal),
    path('localhost/admin/',Pagina_principal)
    
]
