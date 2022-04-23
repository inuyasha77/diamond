# Generated by Django 3.2.12 on 2022-04-11 19:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=150, verbose_name='Nombres')),
                ('dni', models.CharField(max_length=10, unique=True, verbose_name='Dni')),
                ('date_joined', models.DateField(default=datetime.datetime(2022, 4, 11, 14, 20, 58, 194069), verbose_name='fecha de registro')),
                ('date_creation', models.DateTimeField(auto_now=True)),
                ('date_update', models.DateTimeField(auto_now_add=True)),
                ('age', models.PositiveIntegerField(default=0)),
                ('salary', models.DecimalField(decimal_places=3, default=0.0, max_digits=9)),
                ('state', models.BooleanField(default=True)),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='avatar/%y/%m/%d')),
                ('cvitae', models.FileField(blank=True, null=True, upload_to='cvitae/%y/%m/%d')),
            ],
            options={
                'verbose_name': 'empleado',
                'verbose_name_plural': 'empleados',
                'db_table': 'empleado',
                'ordering': ['id'],
            },
        ),
    ]
