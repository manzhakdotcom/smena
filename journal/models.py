from django.db import models
# Create your models here.


class WriteDown(models.Model):
    date = models.DateField(verbose_name='Дата записи')
    time = models.TimeField(verbose_name='Время записи')
    text = models.TextField(verbose_name='Текст записи')
    creation_date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    is_published = models.BooleanField(verbose_name='Опубликована', default=True)

    def __str__(self):
        return '{}'.format(self.date)

    class Meta:
        verbose_name = 'Запись СЦБ'
        verbose_name_plural = 'Записи СЦБ'


class WriteOutQuerySet(models.QuerySet):
    def is_published(self):
        return self.filter(
            models.Q(is_published=True))


class WriteOut(models.Model):
    date = models.DateField(verbose_name='Дата выписки')
    time = models.TimeField(verbose_name='Время выписки')
    text = models.TextField(verbose_name='Текст выписки')
    write_down = models.ForeignKey(WriteDown, on_delete=models.CASCADE, verbose_name='Запись')
    creation_date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    is_published = models.BooleanField(verbose_name='Опубликована', default=True)

    def __str__(self):
        return '{}'.format(self.date)

    class Meta:
        verbose_name = 'Выписка СЦБ'
        verbose_name_plural = 'Выписки СЦБ'

    objects = WriteOutQuerySet.as_manager()


class ExtraWriteOutQuerySet(models.QuerySet):
    def is_published(self):
        return self.filter(
            models.Q(is_published=True))


class ExtraWriteOut(models.Model):
    date = models.DateField(verbose_name='Дата доп. выписки')
    time = models.TimeField(verbose_name='Время доп. выписки')
    text = models.TextField(verbose_name='Текст доп. выписки')
    write_down = models.ForeignKey('WriteDown', on_delete=models.CASCADE, verbose_name='Запись')
    creation_date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    is_published = models.BooleanField(verbose_name='Опубликована', default=True)

    def __str__(self):
        return '{}'.format(self.date)

    class Meta:
        verbose_name = 'Доп. выписка СЦБ'
        verbose_name_plural = 'Доп. выписка СЦБ'

    objects = ExtraWriteOutQuerySet.as_manager()
