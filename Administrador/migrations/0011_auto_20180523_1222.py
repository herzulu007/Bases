# Generated by Django 2.0.4 on 2018-05-23 17:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Administrador', '0010_auto_20180523_1215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funcionario',
            name='Cargo',
            field=models.OneToOneField(default='0', on_delete=django.db.models.deletion.CASCADE, to='Administrador.Cargos'),
        ),
    ]
