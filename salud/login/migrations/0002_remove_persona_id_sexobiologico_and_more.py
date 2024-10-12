# Generated by Django 5.1.2 on 2024-10-11 05:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_tipo_examen'),
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='persona',
            name='id_sexobiologico',
        ),
        migrations.AddField(
            model_name='persona',
            name='id_sexo_biologico',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.sexo_biologico'),
        ),
    ]