# Generated by Django 2.0.4 on 2018-05-20 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Administrador', '0005_auto_20180519_1134'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cargos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Lugar_de_trabajo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='funcionario',
            name='Cargo',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
    ]
