# Generated by Django 3.2.13 on 2022-05-31 18:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('curso', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='curso',
            old_name='nome_do_curso',
            new_name='nome',
        ),
    ]

