from django.db import models
from django.utils import timezone
# Create your models here.


class WriteOut(models.Model):
    date_created = models.DateField(verbose_name='Дата выписки', default=timezone.now)
    write_out = models.TextField(verbose_name='Выписка', default='Выписка...')
    write_down = models.ForeignKey('WriteDown', on_delete=models.CASCADE, verbose_name='Запись')
    delete = models.BooleanField(default=False, verbose_name='Удалена')

    def __str__(self):
        return '{}'.format(self.date_created)

    class Meta:
        verbose_name = 'Выписка СЦБ'
        verbose_name_plural = 'Выписки СЦБ'


class WriteDown(models.Model):
    date_created = models.DateField(verbose_name='Дата записи', default=timezone.now)
    write_down = models.TextField(verbose_name='Текст записи', default='Запись...')
    delete = models.BooleanField(default=False, verbose_name='Удалена')

    def __str__(self):
        return '{}'.format(self.date_created)

    class Meta:
        verbose_name = 'Запись СЦБ'
        verbose_name_plural = 'Записи СЦБ'


class ExtraWriteOut(models.Model):
    date_created = models.DateField(verbose_name='Дата доп. выписки', default=timezone.now)
    extra_write_out = models.TextField(verbose_name='Доп. выписка', default='Доп. выписка...')
    write_down = models.ForeignKey('WriteDown', on_delete=models.CASCADE, verbose_name='Запись')
    delete = models.BooleanField(default=False, verbose_name='Удалена')

    def __str__(self):
        return '{}'.format(self.date_created)

    class Meta:
        verbose_name = 'Доп. выписка СЦБ'
        verbose_name_plural = 'Доп. выписка СЦБ'
