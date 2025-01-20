# expenses/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Sum
from .models import Departamento, Empleado, Gasto
from .forms import DepartamentoForm, EmpleadoForm, GastoForm, FiltroFechaForm

def index(request):
    form = FiltroFechaForm(request.GET or None)
    gastos = None
    resumen_departamentos = None

    if form.is_valid():
        fecha_inicio = form.cleaned_data['fecha_inicio']
        fecha_fin = form.cleaned_data['fecha_fin']
        
        gastos = Gasto.objects.filter(
            fecha__gte=fecha_inicio,
            fecha__lte=fecha_fin
        ).order_by('fecha')
        
        resumen_departamentos = gastos.values('departamento__dept').annotate(
            total=Sum('monto')
        ).order_by('departamento__dept')

    return render(request, 'expenses/index.html', {
        'form': form,
        'gastos': gastos,
        'resumen_departamentos': resumen_departamentos,
    })

# CRUD Departamento
def departamento_list(request):
    departamentos = Departamento.objects.all().order_by('dept')
    return render(request, 'expenses/departamento_list.html', {'departamentos': departamentos})

def departamento_create(request):
    if request.method == 'POST':
        form = DepartamentoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('departamento_list')
    else:
        form = DepartamentoForm()
    return render(request, 'expenses/departamento_form.html', {'form': form, 'action': 'Crear'})

def departamento_update(request, pk):
    departamento = get_object_or_404(Departamento, pk=pk)
    if request.method == 'POST':
        form = DepartamentoForm(request.POST, instance=departamento)
        if form.is_valid():
            form.save()
            return redirect('departamento_list')
    else:
        form = DepartamentoForm(instance=departamento)
    return render(request, 'expenses/departamento_form.html', {'form': form, 'action': 'Editar'})

def departamento_delete(request, pk):
    departamento = get_object_or_404(Departamento, pk=pk)
    if request.method == 'POST':
        departamento.delete()
        return redirect('departamento_list')
    return render(request, 'expenses/departamento_confirm_delete.html', {'departamento': departamento})

# CRUD Empleado
def empleado_list(request):
    empleados = Empleado.objects.all().order_by('nombre')
    return render(request, 'expenses/empleado_list.html', {'empleados': empleados})

def empleado_create(request):
    if request.method == 'POST':
        form = EmpleadoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('empleado_list')
    else:
        form = EmpleadoForm()
    return render(request, 'expenses/empleado_form.html', {'form': form, 'action': 'Crear'})

def empleado_update(request, pk):
    empleado = get_object_or_404(Empleado, pk=pk)
    if request.method == 'POST':
        form = EmpleadoForm(request.POST, instance=empleado)
        if form.is_valid():
            form.save()
            return redirect('empleado_list')
    else:
        form = EmpleadoForm(instance=empleado)
    return render(request, 'expenses/empleado_form.html', {'form': form, 'action': 'Editar'})

def empleado_delete(request, pk):
    empleado = get_object_or_404(Empleado, pk=pk)
    if request.method == 'POST':
        empleado.delete()
        return redirect('empleado_list')
    return render(request, 'expenses/empleado_confirm_delete.html', {'empleado': empleado})

# CRUD Gasto
def gasto_list(request):
    gastos = Gasto.objects.all().order_by('-fecha')
    return render(request, 'expenses/gasto_list.html', {'gastos': gastos})

def gasto_create(request):
    if request.method == 'POST':
        form = GastoForm(request.POST)
        if form.is_valid():
            gasto = form.save(commit=False)
            # Aseguramos que el departamento coincida con el del empleado
            gasto.departamento = gasto.empleado.departamento
            gasto.save()
            return redirect('gasto_list')
    else:
        form = GastoForm()
    return render(request, 'expenses/gasto_form.html', {'form': form, 'action': 'Crear'})

def gasto_update(request, pk):
    gasto = get_object_or_404(Gasto, pk=pk)
    if request.method == 'POST':
        form = GastoForm(request.POST, instance=gasto)
        if form.is_valid():
            gasto = form.save(commit=False)
            gasto.departamento = gasto.empleado.departamento
            gasto.save()
            return redirect('gasto_list')
    else:
        form = GastoForm(instance=gasto)
    return render(request, 'expenses/gasto_form.html', {'form': form, 'action': 'Editar'})

def gasto_delete(request, pk):
    gasto = get_object_or_404(Gasto, pk=pk)
    if request.method == 'POST':
        gasto.delete()
        return redirect('gasto_list')
    return render(request, 'expenses/gasto_confirm_delete.html', {'gasto': gasto})