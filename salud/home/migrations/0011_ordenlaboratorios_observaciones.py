# Generated by Django 5.1.2 on 2024-10-14 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_alter_persona_nombre2'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordenlaboratorios',
            name='observaciones',
            field=models.CharField(db_default='Sin Observacion', max_length=300),
        ),
    ]
