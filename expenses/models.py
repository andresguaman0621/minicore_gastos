# expenses/models.py
from django.db import models

class Departamento(models.Model):
    dept = models.CharField(max_length=100)

    def __str__(self):
        return self.dept

    class Meta:
        verbose_name = 'Departamento'
        verbose_name_plural = 'Departamentos'

class Empleado(models.Model):
    nombre = models.CharField(max_length=100)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'

class Gasto(models.Model):
    fecha = models.DateField()
    descripcion = models.CharField(max_length=200)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.fecha} - {self.descripcion} - {self.monto}"

    class Meta:
        verbose_name = 'Gasto'
        verbose_name_plural = 'Gastos'