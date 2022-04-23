from django.db import models
from datetime import datetime

# Create your models here.

class Type(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre', unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'tipo'
        verbose_name_plural = 'tipos'
        db_table = 'tipo'
        ordering = ['id']

class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'
        db_table = 'categoria'
        ordering = ['id']

class Employee(models.Model):
    categ = models.ManyToManyField(Category)
    type =models.ForeignKey(Type, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=150, verbose_name='Nombres')
    dni = models.CharField(max_length=10, unique=True, verbose_name='Dni')
    date_joined = models.DateField(default=datetime.now, verbose_name='fecha de registro')
    date_creation = models.DateTimeField(auto_now=True)
    date_update = models.DateTimeField(auto_now_add=True)
    age = models.PositiveIntegerField(default=0)
    salary = models.DecimalField(default=0.000, max_digits=9, decimal_places=3)
    state = models.BooleanField(default=True)
    avatar = models.ImageField(upload_to='avatar/%y/%m/%d', null=True, blank=True)
    cvitae = models.FileField(upload_to='cvitae/%y/%m/%d', null=True, blank=True)

    def __str__(self):
        return self.field_names



    class Meta:
        verbose_name = 'empleado'
        verbose_name_plural = 'empleados'
        db_table = 'empleado'
        ordering = ['id']
