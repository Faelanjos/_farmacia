from django.urls import path

from sistema import views 

app_name = 'sistema'

urlpatterns = [
    path('', views.index, name='index'),
    path('cliente/', views.listarClientes, name='cliente'),
    path('cliente/perfil/<int:cliente_id>', views.perfilCliente, name='perfilCliente'),
    path('cliente/novo/', views.criarCliente, name='criar_cliente'),
    path('funcionario/', views.listarFuncionarios, name='funcionario'),
    path('funcionario/perfil/<int:funcionario_id>', views.perfilFuncionario, name='perfilFuncionario'),
    path('funcionario/novo/', views.criarFuncionario, name='criar_funcionario'),
    path('medicamento/', views.listarMedicamentos, name='medicamento'),
    path('medicamento/perfil/<int:medicamento_id>', views.perfilMedicamento, name='perfilMedicamento'),
    path('medicamento/novo/', views.criarMedicamento, name='criar_medicamento'),
    path('fornecedor/', views.listarFornecedor, name='fornecedor'),
    path('fornecedor/perfil/<int:fornecedor_id>', views.perfilFornecedor, name='perfilFornecedor'),
    path('fornecedor/novo/', views.criarFornecedor, name='criar_fornecedor'),
]