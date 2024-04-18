# Generated by Django 3.2.24 on 2024-04-15 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BusStation', '0012_auto_20240415_1036'),
    ]

    operations = [
        migrations.AddField(
            model_name='busroute',
            name='cost',
            field=models.IntegerField(default=1000, verbose_name='Цена одного билета'),
        ),
        migrations.AddField(
            model_name='passenger',
            name='balance',
            field=models.IntegerField(default=0, verbose_name='Баланс счёта'),
        ),
    ]