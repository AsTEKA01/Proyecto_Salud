# Generated by Django 5.1.2 on 2024-10-12 00:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0007_alter_persona_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='nombre2',
            field=models.CharField(default='No especificado', max_length=50),
        ),
    ]