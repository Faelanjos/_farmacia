from django.shortcuts import render, redirect, get_object_or_404
from sistema.models import Medicamento
from sistema.forms import MedicamentoForm

def listarMedicamentos(request):
    medicamentos = Medicamento.objects.all() 

    context = { 
        'medicamentos' : medicamentos,
    }
    
    return render(
        request,
        'medicamento/listar.html',
        context,

    )

def criarMedicamento(request):
    if request.method == 'POST':

        form = MedicamentoForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('/medicamentos')
        
    else:

        form = MedicamentoForm()

    return render(
        request,
        'medicamento/cadastro.html',
        {'form': form}
    )

#View referente aos detalhes(perfil) do medicamento
def perfilMedicamento(request, medicamento_id):
    medicamentoUnico = get_object_or_404( #método utilizado para mostrar o medicamento ou exibir erro 404
        Medicamento, pk=medicamento_id #medicamento é o model, pc=medicamento_id está definido através de qual campo(coluna) o objeto será retornado
    )
    titulo = f'{medicamentoUnico.nome} ' #Cria um título com nome e sobranome do medicamento atual
    context = { #declaração de um dict que possui a chave medicamentos e o valor medicamentos (variavel criada acima)
        'medicamentoUnico' : medicamentoUnico,
        'titulo': titulo,
    }


    return render(
        request,
        'medicamento/perfil.html',
        context,

    )