# Generated by Django 2.0.4 on 2018-05-28 03:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Usuario', '0014_auto_20180527_2228'),
        ('Administrador', '0019_auto_20180526_1111'),
    ]

    operations = [
        migrations.AddField(
            model_name='solicitud',
            name='revisado',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='solicitud',
            name='usuario',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Usuario.Usuario'),
        ),
    ]
