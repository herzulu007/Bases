from django import forms
from Modulos.Usuario.models import Usuario


class Usuario_form(forms.ModelForm):

	class Meta:
		model = Usuario

		fields = [
			'Cedula',
			'Nombre1',
			'Nombre2',
			'tipo_solicitud',
			'created_date',
			
		]
		
		labels = {
			'Cedula' : 'Cedula',
			'Nombre1' : 'Primer Nombre',
			'Nombre2' : 'Primer Nombre',
			'tipo_solicitud' : 'tipo_solicitud',
			'created_date' : 'dia de creacion',
		
		}	

		widgets = {

			'Cedula' : forms.TextInput(attrs={'class':'form_control'}),
			'Nombre1': forms.TextInput(attrs={'class':'form_control'}),
			'Nombre2': forms.TextInput(attrs={'class':'form_control'}),
			'tipo_solicitud': forms.TextInput(attrs={'class':'form_control'}),
			'created_date': forms.TextInput(attrs={'class':'form_control'}),
			

		}