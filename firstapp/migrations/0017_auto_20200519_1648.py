# Generated by Django 3.0.6 on 2020-05-19 13:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0016_auto_20200519_1607'),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name='author',
            name='firstapp_au_name_37a1ac_gin',
        ),
        migrations.RemoveIndex(
            model_name='genre',
            name='firstapp_ge_name_c568fd_gin',
        ),
    ]