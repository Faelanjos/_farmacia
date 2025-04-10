from django.db import models

from django.utils import timezone


class Cargo(models.Model):
    nome = models.CharField(max_length = 50)


    def __str__(self):
        return f'{self.nome}'


class Plano_de_Saude(models.Model):
    nome = models.CharField(max_length = 50)
    desconto = models.DecimalField(max_digits=4, decimal_places=2,null = True)



class Funcionario(models.Model):
    nome = models.CharField(max_length = 50)
    sobrenome = models.CharField(max_length = 50)
    cpf = models.CharField(max_length = 11, unique=True)
    idade = models.CharField(max_length = 3)
    email = models.EmailField()
    telefone = models.CharField(max_length = 12)
    cadastro = models.DateTimeField(default=timezone.now)
    salario = models.DecimalField(max_digits=8, decimal_places=2)
    cargo = models.ForeignKey(Cargo, blank=True, on_delete=models.CASCADE)


    def __str__(self):
        return f'{self.nome} {self.sobrenome}'



class Cliente(models.Model):
    nome = models.CharField(max_length = 50)
    sobrenome = models.CharField(max_length = 50)
    cpf = models.CharField(max_length = 11, unique=True)
    idade = models.CharField(max_length = 3)
    email = models.EmailField()
    telefone = models.CharField(max_length = 12)
    cadastro = models.DateTimeField(default=timezone.now)
    cep = models.CharField(max_length = 8)
    endereco = models.TextField(blank=False)
    mensagem = models.TextField(blank=True)
    convenio = models.ForeignKey(Plano_de_Saude, null = True, on_delete=models.CASCADE)



    def __str__(self):
        return f'{self.nome} {self.sobrenome}'
    
class Fornecedor(models.Model):
    nome = models.CharField(max_length = 50)
    cnpj = models.CharField(max_length = 20, null =True)


    def __str__(self):
        return f'{self.nome} '

    
class Medicamento(models.Model):
    nome = models.CharField(max_length = 50)
    preco = models.DecimalField(max_digits=5, decimal_places=2)
    receita = models.BooleanField(default=True)
    estoque = models.IntegerField()
    op_desconto = models.BooleanField(default = False)
    fornecedor = models.ForeignKey(Fornecedor, null = True, on_delete=models.CASCADE)


    def __str__(self):
        return f'{self.nome}'