from django.contrib import admin
from sistema import models

@admin.register(models.Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'sobrenome', 'cargo', 'email', 'telefone',)
    search_fields = ('id', 'nome', 'sobrenome', 'email', 'cargo',)



@admin.register(models.Cargo)
class CargoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome',)
    search_fields = ('id', 'nome',)


@admin.register(models.Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'sobrenome', 'email', 'telefone',)
    search_fields = ('id', 'nome',)


@admin.register(models.Medicamento)
class MedicamentoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'preco', 'receita', 'op_desconto',)
    list_editable = ('receita','op_desconto',)
    search_fields = ('id', 'nome',)


@admin.register(models.Plano_de_Saude)
class Plano_de_SaudeAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome',)

@admin.register(models.Fornecedor)
class FornecedorAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'cnpj',)
    search_fields = ('id', 'nome',)