from django.db import models
from django.utils import timezone
# Create your models here.
from datetime import date


class Lugar(models.Model):
	Nombre = models.CharField(max_length=100)

	def __str__(self):
		return self.Nombre



class Usuario(models.Model):
	##id = models.CharField(max_length=10,primary_key = True)
	Identificacion = models.CharField(max_length=20)
	Nombre = models.CharField(max_length=20)
	tipo_solicitud = models.CharField(max_length=20)
	created_date = models.DateTimeField(default=date.today)
	email = models.EmailField(max_length=40)
	
	def __str__(self):
		return self.Nombre


