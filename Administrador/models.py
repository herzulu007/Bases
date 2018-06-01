from django.db import models
from django.utils import timezone
# Create your models here.
from datetime import date
from Modulos.Usuario.models import Usuario



class Cargos(models.Model):
	"""docstring for Cargos"""
	id_Cargo = models.AutoField(primary_key=True)
	Nombre= models.CharField(max_length=20)

	def __str__(self):
		return self.Nombre
		

class Lugar(models.Model):
	id_lugar = models.AutoField(primary_key=True)
	Nombre = models.CharField(max_length=100)
	
	def __str__(self):
		return self.Nombre

class Cede(models.Model):
	id_Cede = models.AutoField(primary_key=True)
	Nombre = models.CharField(max_length=40)
	lugar = models.OneToOneField(Lugar,on_delete=models.CASCADE) 
 	
	def __str__(self):
		return self.Nombre

class Entidad_emisora(models.Model):
	id_lugar = models.AutoField(primary_key=True)
	Nombre = models.CharField(max_length=100)
	lugar = models.OneToOneField(Lugar,on_delete=models.CASCADE)

	def __str__(self):
		return self.Nombre


class Entidad_receptora(models.Model):
	id_lugar = models.AutoField(primary_key=True)
	Nombre = models.CharField(max_length=100)
	lugar = models.OneToOneField(Lugar,on_delete=models.CASCADE)

	def __str__(self):
		return self.Nombre


class Funcionario(models.Model):
	Cedula = models.CharField(primary_key=True,max_length=10)
	Nombre = models.CharField(max_length=200)
	cede = models.ForeignKey(Cede,on_delete=models.CASCADE)
	cargo = models.ForeignKey(Cargos,on_delete=models.CASCADE)
	Email = models.EmailField(blank=True)
	
	def __str__(self):
		return self.Nombre


class Tipo_solicitud(models.Model):
	id_solicitud = models.AutoField(primary_key=True)
	Nombre =  models.CharField(max_length=50)
	
	def __str__(self):
		return self.Nombre

	
class Solicitud(models.Model):
	Numero_solicitud = models.AutoField(primary_key=True)
	Asunto = models.ForeignKey(Tipo_solicitud,on_delete=models.CASCADE)
	funcionario = models.ForeignKey(Funcionario,null = True ,blank = True,on_delete=models.CASCADE)
	Fecha = models.DateField(default=date.today)
	entidad_emisora = models.ForeignKey(Entidad_emisora,on_delete=models.CASCADE)
	entidad_receptora = models.ForeignKey(Entidad_receptora,on_delete=models.CASCADE)
	usuario = models.ForeignKey(Usuario,null = True ,blank = True,on_delete=models.CASCADE)




	def __str__(self):
		return self.Numero_solicitud




