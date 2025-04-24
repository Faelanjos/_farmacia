from django.shortcuts import render, get_object_or_404, redirect
from sistema.models import Funcionario
from sistema.forms import FuncionarioForm

def listarFuncionarios(request):
    funcionarios = Funcionario.objects.all() 

    context = { 
        'funcionarios' : funcionarios,
    }
    
    return render(
        request,
        'funcionario/listar.html',
        context,

    )

def criarFuncionario(request):
    if request.method == 'POST':

        form = FuncionarioForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('/funcionarios')
        
    else:

        form = FuncionarioForm()

    return render(
        request,
        'funcionario/cadastro.html',
        {'form': form}
    )

#View referente aos detalhes(perfil) do funcionario
def perfilFuncionario(request, funcionario_id):
    funcionarioUnico = get_object_or_404( #método utilizado para mostrar o funcionario ou exibir erro 404
        Funcionario, pk=funcionario_id #funcionario é o model, pc=funcionario_id está definido através de qual campo(coluna) o objeto será retornado
    )
    titulo = f'{funcionarioUnico.nome} {funcionarioUnico.sobrenome}' #Cria um título com nome e sobranome do funcionario atual
    context = { #declaração de um dict que possui a chave funcionarios e o valor funcionarios (variavel criada acima)
        'funcionarioUnico' : funcionarioUnico,
        'titulo': titulo,
    }


    return render(
        request,
        'funcionario/perfil.html',
        context,

    )