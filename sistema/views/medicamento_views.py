from django.shortcuts import render
from sistema.models import Medicamento

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