from django.shortcuts import render, redirect, reverse
from Modulos.Administrador.forms import Lugares_form, Funcionario_form ,Tipo_Solicitud_form,Solicitud_Form
from Modulos.Administrador.models import Funcionario, Tipo_solicitud,Solicitud
# Create your views here.
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

def Pagina_principal(request):
	return render(request,'templates_base/index.html')

def Pagina_principal_funcionario(request):
	return render(request,'Administrador/Main.html')

def Lugar_view(request):
	if request.method == 'POST':
		form = Lugares_form(request.POST)
		if form.is_valid():
			form.save()
		return redirect(reverse('index1'))	
	else:
		form = Lugares_form()
	return render(request,'Administrador/Lugar_form.html',{'form':form})

def Funcionario_view(request):
	if request.method == 'POST':
		form = Funcionario_form(request.POST)
		if form.is_valid():
			form.save()
		return redirect(reverse('index'))	
	else:
		form = Funcionario_form()
	return render(request,'Administrador/Administrador_formulario.html',{'form':form})

def Funcionarios_list(request):

	funcionario = Funcionario.objects.all()
	contexto = {'funcionarios':funcionario}
	return render(request,'Administrador/Administrador_list.html',contexto)


##lista los funcionarios funcionando

class FuncionarioList(ListView):
	model = Funcionario
	template_name = 'Administrador/Administrador_list.html'


class FuncionarioCreate(CreateView):
	model = Funcionario
	form_class =  Funcionario_form
	template_name = 'Administrador/Administrador_formulario.html'
	success_url = reverse_lazy('Funcionarios_inscritos')

class FuncionarioUpdate(UpdateView):
	model = Funcionario
	form_class =  Funcionario_form
	template_name = 'Administrador/Funcionario_form.html'
	success_url = reverse_lazy('index1')





class SolicitudCreate(CreateView):
	model = Solicitud
	form_class = Solicitud_Form
	template_name = 'Administrador/Solicitud_form.html'
	success_url = reverse_lazy('index1')


class SolicitudList(ListView):
	model = Solicitud
	template_name = 'Administrador/Solicitud_list.html'


class Solicitud_update(UpdateView):
	model = Solicitud
	form_class =  Solicitud_Form
	template_name = 'Administrador/Solicitud_form.html'
	success_url = reverse_lazy('index1')


class SolicitudDelete(DeleteView):
	model = Solicitud
	template_name = 'Administrador/Solicitud_borrar.html'
	success_url = reverse_lazy('index1')


class Tipo_SolicitudCreate(CreateView):
	model = Tipo_solicitud
	form_class =  Tipo_Solicitud_form
	template_name = 'Administrador/Tipo_Solicitud_form.html'
	success_url = reverse_lazy('index1')


class Tipo_SolicitudList(ListView):
	model = Tipo_solicitud
	template_name = 'Administrador/Tipo_Solicitud_list.html'




class RegistroFuncionario(CreateView):
	model = User
	template_name = 'Administrador/registrar.html'
	form_class =UserCreationForm
	success_url = reverse_lazy('Solicitudlist')
 		