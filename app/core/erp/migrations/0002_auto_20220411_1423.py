# Generated by Django 3.2.12 on 2022-04-11 19:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='cvitae',
        ),
        migrations.AlterField(
            model_name='employee',
            name='date_joined',
            field=models.DateField(default=datetime.datetime(2022, 4, 11, 14, 23, 32, 432510), verbose_name='fecha de registro'),
        ),
    ]
