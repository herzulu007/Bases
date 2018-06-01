# Generated by Django 2.0.4 on 2018-05-23 18:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Administrador', '0013_auto_20180523_1229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funcionario',
            name='Cargo',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Administrador.Cargos'),
        ),
        migrations.AlterField(
            model_name='funcionario',
            name='Cede',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Administrador.Entidad_emisora'),
        ),
        migrations.AlterField(
            model_name='funcionario',
            name='lugar',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Administrador.Lugar'),
        ),
    ]
