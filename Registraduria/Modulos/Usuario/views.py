from django.shortcuts import render, redirect, reverse
from Modulos.Usuario.forms import Usuario_form 
# Create your views here.

def Pagina_principal_usuario(request):
	return render(request,'Usuario/index.html')



def Usuario_view(request):
	if request.method == 'POST':
		form = Usuario_form(request.POST)
		if form.is_valid():
			form.save()
		return redirect(reverse('index'))	
	else:
		form = Usuario_form()
	return render(request,'Usuario/Usuario_form.html',{'form':form})