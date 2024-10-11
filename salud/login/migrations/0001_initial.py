# Generated by Django 5.1.2 on 2024-10-11 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('tipo_identificacion', models.CharField(choices=[('TI', 'Tarjeta de Identidad'), ('CC', 'Cédula de Ciudadania'), ('CE', 'Cédula de Extranjería')], max_length=20)),
                ('numero_id', models.CharField(max_length=50)),
                ('apellido1', models.CharField(max_length=50)),
                ('apellido2', models.CharField(max_length=50)),
                ('nombre1', models.CharField(max_length=50)),
                ('nombre2', models.CharField(max_length=50)),
                ('fecha_nac', models.DateField()),
                ('id_sexobiologico', models.IntegerField()),
                ('direccion', models.TextField()),
                ('tel_movil', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]