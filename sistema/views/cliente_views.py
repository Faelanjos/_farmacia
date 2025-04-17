from django.shortcuts import render, redirect, get_object_or_404
from sistema.models import Cliente
from sistema.forms import ClienteForm

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

def criarCliente(request):
    if request.method == 'POST':

        form = ClienteForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('/clientes')
        
    else:

        form = ClienteForm()

    return render(
        request,
        'cliente/cadastro.html',
        {'form': form}
    )