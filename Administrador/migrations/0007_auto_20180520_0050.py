# Generated by Django 2.0.4 on 2018-05-20 05:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Administrador', '0006_auto_20180520_0044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funcionario',
            name='Cargo',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Administrador.Cargos'),
        ),
    ]
