from django.db import models
from django.utils import timezone
# Create your models here.

class Usuario(models.Model):
	Cedula =models.CharField(max_length=20,primary_key =True)
	Nombre1 = models.CharField(max_length=20)
	Nombre2 = models.CharField(max_length=20)
	#Apellido2 = models.CharField(max_length=20)
	tipo_solicitud = models.CharField(max_length=20)
	created_date = models.DateTimeField(default=timezone.now)
    
	def __str__(self):
		return self.Nombre1