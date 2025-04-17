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