from django.urls import path

from sistema import views 

app_name = 'sistema'

urlpatterns = [
    path('cliente/', views.listarClientes, name='cliente'),
    path('funcionario/', views.listarFuncionarios, name='funcionario'),
    path('medicamento/', views.listarMedicamentos, name='medicamento'),
]