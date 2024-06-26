# Generated by Django 3.2.24 on 2024-04-19 03:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('BusStation', '0013_auto_20240415_1321'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comfort',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100, verbose_name='Название')),
                ('desc', models.TextField(default='', verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Класс комфорта',
                'verbose_name_plural': 'Класс комфорта',
            },
        ),
        migrations.AddField(
            model_name='busroute',
            name='comfort',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='BusStation.comfort'),
        ),
    ]
