from django.shortcuts import render, redirect, get_object_or_404
from sistema.models import Fornecedor
from sistema.forms import FornecedorForm


def listarFornecedor(request):
    fornecedores = Fornecedor.objects.all() 

    context = { 
        'fornecedores' : fornecedores,
    }
    
    return render(
        request,
        'fornecedor/listar.html',
        context,

    )

def criarFornecedor(request):
    if request.method == 'POST':

        form = FornecedorForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('/fornecedores')
        
    else:

        form = FornecedorForm()

    return render(
        request,
        'fornecedor/cadastro.html',
        {'form': form}
    )


#View referente aos detalhes(perfil) do paciente
def perfilFornecedor(request, fornecedor_id):
    fornecedorUnico = get_object_or_404( #método utilizado para mostrar o fornecedor ou exibir erro 404
        Fornecedor, pk=fornecedor_id #fornecedor é o model, pc=fornecedor_id está definido através de qual campo(coluna) o objeto será retornado
    )
    titulo = f'{fornecedorUnico.nome}' #Cria um título com nome e sobranome do fornecedor atual
    context = { #declaração de um dict que possui a chave fornecedors e o valor fornecedors (variavel criada acima)
        'fornecedorUnico' : fornecedorUnico,
        'titulo': titulo,
    }


    return render(
        request,
        'fornecedor/perfil.html',
        context,

    )