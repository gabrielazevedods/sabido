# Generated by Django 3.2.13 on 2022-07-16 22:51

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projeto', '0001_initial'),
        ('tarefa', '0002_auto_20220528_1332'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tarefa',
            old_name='data_tarefa',
            new_name='data_fim_tarefa',
        ),
        migrations.RemoveField(
            model_name='tarefa',
            name='disciplina',
        ),
        migrations.AddField(
            model_name='tarefa',
            name='data_inicio_tarefa',
            field=models.DateField(default=datetime.datetime(2022, 7, 19, 0, 0)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tarefa',
            name='projeto',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='projeto.projeto'),
            preserve_default=False,
        ),
    ]

