# expenses/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    
    # URLs para Departamento
    path('departamentos/', views.departamento_list, name='departamento_list'),
    path('departamentos/crear/', views.departamento_create, name='departamento_create'),
    path('departamentos/<int:pk>/editar/', views.departamento_update, name='departamento_update'),
    path('departamentos/<int:pk>/eliminar/', views.departamento_delete, name='departamento_delete'),
    
    # URLs para Empleado
    path('empleados/', views.empleado_list, name='empleado_list'),
    path('empleados/crear/', views.empleado_create, name='empleado_create'),
    path('empleados/<int:pk>/editar/', views.empleado_update, name='empleado_update'),
    path('empleados/<int:pk>/eliminar/', views.empleado_delete, name='empleado_delete'),
    
    # URLs para Gasto
    path('gastos/', views.gasto_list, name='gasto_list'),
    path('gastos/crear/', views.gasto_create, name='gasto_create'),
    path('gastos/<int:pk>/editar/', views.gasto_update, name='gasto_update'),
    path('gastos/<int:pk>/eliminar/', views.gasto_delete, name='gasto_delete'),
]