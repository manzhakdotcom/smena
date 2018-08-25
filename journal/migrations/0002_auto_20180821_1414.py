# Generated by Django 2.1 on 2018-08-21 11:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='writeout',
            name='data_created',
        ),
        migrations.AddField(
            model_name='writeout',
            name='date_created',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]