from django.shortcuts import render
from sistema.models import Cliente

def listarClientes(request):
    clientes = Cliente.objects.all() 

    context = { 
        'clientes' : clientes,
    }
    
    return render(
        request,
        'cliente/listar.html',
        context,

    )