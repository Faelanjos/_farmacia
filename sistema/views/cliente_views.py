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

#View referente aos detalhes(perfil) do paciente
def perfilCliente(request, cliente_id):
    clienteUnico = get_object_or_404( #método utilizado para mostrar o cliente ou exibir erro 404
        Cliente, pk=cliente_id #cliente é o model, pc=cliente_id está definido através de qual campo(coluna) o objeto será retornado
    )
    titulo = f'{clienteUnico.nome} {clienteUnico.sobrenome}' #Cria um título com nome e sobranome do cliente atual
    context = { #declaração de um dict que possui a chave clientes e o valor clientes (variavel criada acima)
        'clienteUnico' : clienteUnico,
        'titulo': titulo,
    }


    return render(
        request,
        'cliente/perfil.html',
        context,

    )