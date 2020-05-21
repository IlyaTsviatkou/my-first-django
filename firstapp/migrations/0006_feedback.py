# Generated by Django 3.0.6 on 2020-05-18 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0005_auto_20200518_1806'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_reply', models.BooleanField(verbose_name='Отправить ответ на e-mail')),
                ('email_adress', models.CharField(blank=True, max_length=500, verbose_name='e-mail адрес для ответа')),
                ('email_reply_capt', models.CharField(blank=True, max_length=500, verbose_name='Заголовок ответа на e-mail')),
                ('email_reply_text', models.TextField(blank=True, null=True, verbose_name='Текст ответа на e-mail')),
            ],
        ),
    ]
