# Generated by Django 2.0.4 on 2018-05-19 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Administrador', '0004_auto_20180501_0035'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='funcionario',
            name='id',
        ),
        migrations.AlterField(
            model_name='funcionario',
            name='Cedula',
            field=models.CharField(max_length=20, primary_key=True, serialize=False),
        ),
    ]