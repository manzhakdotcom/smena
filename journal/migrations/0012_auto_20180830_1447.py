# Generated by Django 2.1 on 2018-08-30 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0011_merge_20180829_1852'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='extrawriteout',
            name='extra_write_out',
        ),
        migrations.RemoveField(
            model_name='writedown',
            name='write_down',
        ),
        migrations.RemoveField(
            model_name='writeout',
            name='write_down_id',
        ),
        migrations.RemoveField(
            model_name='writeout',
            name='write_out',
        ),
        migrations.AddField(
            model_name='extrawriteout',
            name='text',
            field=models.TextField(default='Доп. выписка...', verbose_name='Текст доп. выписки'),
        ),
        migrations.AddField(
            model_name='writedown',
            name='text',
            field=models.TextField(default='Запись...', verbose_name='Текст записи'),
        ),
        migrations.AddField(
            model_name='writeout',
            name='text',
            field=models.TextField(default='Выписка...', verbose_name='Текст выписки'),
        ),
    ]
