# Generated by Django 3.2.24 on 2024-03-28 07:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('BusStation', '0007_raspisaniereisov'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='date_of_departure',
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='station_of_arrived',
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='station_of_departure',
        ),
        migrations.AddField(
            model_name='ticket',
            name='route',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='BusStation.raspisaniereisov'),
        ),
    ]
