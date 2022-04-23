# Generated by Django 3.2.12 on 2022-04-11 23:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0003_alter_employee_date_joined'),
    ]

    operations = [
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Nombre')),
            ],
        ),
        migrations.AddField(
            model_name='employee',
            name='type',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='erp.type'),
            preserve_default=False,
        ),
    ]
