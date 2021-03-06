# Generated by Django 2.1 on 2018-08-23 12:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0009_auto_20180823_1516'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='extrawriteout',
            name='write_down_id',
        ),
        migrations.RemoveField(
            model_name='writeout',
            name='write_down_id',
        ),
        migrations.AddField(
            model_name='extrawriteout',
            name='write_down',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='journal.WriteDown', verbose_name='Запись'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='writeout',
            name='write_down',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='journal.WriteDown', verbose_name='Запись'),
            preserve_default=False,
        ),
    ]
