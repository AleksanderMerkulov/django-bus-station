# Generated by Django 3.2.24 on 2024-03-28 07:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('BusStation', '0008_auto_20240328_1710'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ticketnologin',
            options={'verbose_name': 'Билет без регистрации', 'verbose_name_plural': 'Билеты без регистрации'},
        ),
        migrations.RemoveField(
            model_name='ticketnologin',
            name='date_of_departure',
        ),
        migrations.RemoveField(
            model_name='ticketnologin',
            name='station_of_arrived',
        ),
        migrations.RemoveField(
            model_name='ticketnologin',
            name='station_of_departure',
        ),
        migrations.AddField(
            model_name='passenger',
            name='passengerFIO',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='passenger',
            name='passengerFIO_passport',
            field=models.CharField(blank=True, max_length=11, null=True),
        ),
        migrations.AddField(
            model_name='ticketnologin',
            name='route',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='BusStation.raspisaniereisov'),
        ),
        migrations.AlterField(
            model_name='passenger',
            name='person',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]
