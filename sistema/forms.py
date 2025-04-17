from django import forms
from .models import Cliente
from .models import Medicamento
from .models import Funcionario
from .models import Fornecedor

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = [ 'nome', 'sobrenome', 'email', 'telefone',]


class MedicamentoForm(forms.ModelForm):
    class Meta:
        model = Medicamento
        fields = ['nome', 'preco', 'estoque',]


class FuncionarioForm(forms.ModelForm):
    class Meta:
        model = Funcionario
        fields = [ 'nome', 'sobrenome', 'email', 'telefone', 'cargo',]


class FornecedorForm(forms.ModelForm):
    class Meta:
        model = Fornecedor
        fields = [ 'nome', 'cnpj',]