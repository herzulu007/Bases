# Generated by Django 2.0.4 on 2018-05-25 20:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Administrador', '0017_auto_20180524_1846'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funcionario',
            name='cargo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Administrador.Cargos'),
        ),
        migrations.AlterField(
            model_name='funcionario',
            name='cede',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Administrador.Cede'),
        ),
    ]