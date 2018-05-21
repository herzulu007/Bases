from django.db import models
from django.utils import timezone
# Create your models here.

class Cargos(models.Model):
	"""docstring for Cargos"""
	Nombre= models.CharField(max_length=20)

	def __init__(self):
		return self.Nombre
		

class Lugar_de_trabajo(models.Model):
	Nombre = models.CharField(max_length=100)

	def __str__(self):
		return self.Nombre



class Funcionario(models.Model):
	Cedula = models.CharField(max_length=20,primary_key=True)
	Nombre = models.CharField(max_length=200)
	Cargo = models.OneToOneField(Cargos,on_delete=models.CASCADE)
	
	def __str__(self):
		return self.Nombre
