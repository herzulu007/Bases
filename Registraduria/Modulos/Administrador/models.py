from django.db import models
from django.utils import timezone
# Create your models here.

class Funcionario(models.Model):
	Cedula = models.CharField(max_length=20,primary_key=True)
	Nombre = models.CharField(max_length=200)
	##Tuncionario = models.CharField(max_length=20)



