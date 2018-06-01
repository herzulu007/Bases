from django.urls import path
from Modulos.Administrador.views import Pagina_principal_funcionario, Lugar_view
from Modulos.Administrador.views import Funcionarios_list,Funcionario_view,\
	FuncionarioList,FuncionarioCreate, Tipo_SolicitudCreate,Tipo_SolicitudList,\
	Solicitud_update,SolicitudCreate,SolicitudDelete,SolicitudList,\
    RegistroFuncionario

from Modulos.Usuario.views import Solicitudes_edit
from django.contrib.auth.decorators import login_required



urlpatterns = [
    path('', Pagina_principal_funcionario,name='index1'),
    path('lugares/',login_required(Lugar_view),name='lugar_main'),
    path('inscritos/',login_required(FuncionarioList.as_view()),name='Funcionarios_inscritos'),
    path('nuevo/',login_required(FuncionarioCreate.as_view()),name='Funcionario_nuevo'),
    path('solicitudcreate/',login_required(SolicitudCreate.as_view()),name='SolicitudCreate'),
    path('solicitudlist/',login_required(SolicitudList.as_view()),name='Solicitudlist'),
    path('editar/<int:pk>/',login_required(Solicitud_update.as_view()),name='Editar_solicitud'),
    path('nuevo_tipo_solicitud',login_required(Tipo_SolicitudCreate.as_view()),name='nuevo_tipo_solicitud'),
    path('Tipo_Solicitud_List',login_required(Tipo_SolicitudList.as_view()),name='Tipo_Solicitud_List'),
    path('eliminar_solicitud/<int:pk>/',login_required(SolicitudDelete.as_view()),name='Borrar_solicitud'),
    path('registrar',login_required(RegistroFuncionario.as_view()),name='registrar'),
    
]
