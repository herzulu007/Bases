from django import forms
from Modulos.Usuario.models import Usuario


class Usuario_form(forms.ModelForm):

	class Meta:
		model = Usuario

		fields = [
			'Identificacion',
			'Nombre',
			'tipo_solicitud',
			'created_date',
			'email'
		]
		
		labels = {
			'Identificacion' : 'Cedula',
			'Nombre' : 'Primer Nombre',
			'tipo_solicitud' : 'Tipo solicitud',
			'created_date' : 'dia de creacion',
			'email' : 'email'
		
		}	

		widgets = {

			'Cedula' : forms.TextInput(attrs={'class':'form_control'}),
			'Nombre': forms.TextInput(attrs={'class':'form_control'}),
			'tipo_solicitud': forms.TextInput(attrs={'class':'form_control'}),
			'created_date': forms.TextInput(attrs={'class':'form_control'}),
			'email' : forms.EmailInput(attrs={'class':'form_control'})
			

		}