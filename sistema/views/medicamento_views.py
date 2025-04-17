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