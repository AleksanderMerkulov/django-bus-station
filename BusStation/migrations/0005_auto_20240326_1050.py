# Generated by Django 3.2.24 on 2024-03-26 00:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BusStation', '0004_auto_20240324_1404'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='passengerFIO',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='ticket',
            name='passengerFIO_passport',
            field=models.CharField(blank=True, max_length=11, null=True),
        ),
    ]
