from django import forms
from Modulos.Administrador.models import Lugar,Funcionario, Tipo_solicitud,Solicitud

class Lugares_form(forms.ModelForm):
	class Meta:
		"""docstring for meta"""
		model = Lugar

		
		fields = [
		'Nombre'
		]
		labels = {
		'Nombre' : 'Nombre del lugar'
		}
		widgets = {
		'Nombre': forms.TextInput(attrs={'class':'form_control'})
		}


class Funcionario_form(forms.ModelForm):
	class Meta:

		model = Funcionario
		
		fields = "__all__"
		
		fields =['Cedula','Nombre','cede','cargo','Email']
		labels ={'Cedula' : 'Cedula','Nombre' : 'Nombre'  ,'cede':'cede','cargo':'cargo',
		'Email':'email'}
		widgets = {'Cedula':forms.NumberInput(attrs={'class':'form_control'}),
		'Nombre':forms.TextInput(attrs={'class':'form_control'}),
		'cede':forms.Select(attrs={'class':'form_control'}),
		'cargo':forms.Select(attrs={'class':'form_control'}),
		'email':forms.EmailInput(attrs={'class':'form_control'}),
		}


class Tipo_Solicitud_form(forms.ModelForm):
	class Meta:

		model = Tipo_solicitud

		fields = [
	
		'Nombre'
		]
		labels = {
		
		'Nombre' : 'Tipo de solicitud ',
		}
		widgets = {

		'Nombre': forms.TextInput(attrs={'class':'form_control'})
		}


class Solicitud_Form(forms.ModelForm):
	class Meta:

		model = Solicitud

		fields = [

			
			'Asunto',
			'funcionario',
			'Fecha',
			'entidad_emisora',
			'entidad_receptora',
			'usuario',
			
			]	


		labels = {


		'Asunto':'Asunto',
		'funcionario':'Funcionario quien atiende',
		'Fecha':'Fecha',
		'entidad_emisora ':'Entidad emisora',
		'entidad_receptora':'Entidad receptora',
		'usuario':'Nombre de usuario',
		
		}


		widgets = {

		
		'Asunto' : forms.Select(attrs={'class':'form_control'}),
		'funcionario':forms.Select(attrs={'class':'form_control'}),
		'Fecha':forms.TextInput(attrs={'class':'form_control'}),
		'entidad_emisora ':forms.Select(attrs={'class':'form_control'}),
		'entidad_receptora':forms.Select(attrs={'class':'form_control'}),
		'usuario':forms.Select(attrs={'class':'form_control'}),
		

		}