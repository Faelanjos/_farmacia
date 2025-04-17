from django.urls import path

from sistema import views 

app_name = 'sistema'

urlpatterns = [
    path('cliente/', views.listarClientes, name='cliente'),
    path('cliente/novo/', views.criarCliente, name='criar_cliente'),
    path('funcionario/', views.listarFuncionarios, name='funcionario'),
    path('funcionario/novo/', views.criarFuncionario, name='criar_funcionario'),
    path('medicamento/', views.listarMedicamentos, name='medicamento'),
    path('medicamento/novo/', views.criarMedicamento, name='criar_medicamento'),
    
]