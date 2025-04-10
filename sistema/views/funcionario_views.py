from django.shortcuts import render
from sistema.models import Funcionario

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