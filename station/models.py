from django.db import models

# Create your models here.


class Circle(models.Model):
    name = models.CharField(max_length=128, verbose_name='Название круга')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Диспетчерский круг'
        verbose_name_plural = 'Диспетчерские круги'


class SHCH(models.Model):
    name = models.CharField(max_length=128, verbose_name='Название')
    abbr = models.CharField(max_length=128, verbose_name='Аббревиатура')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Дистанция сигнализации и связи'
        verbose_name_plural = 'Дистанции сигнализации и связи'


class Station(models.Model):
    name = models.CharField(max_length=128, verbose_name='Название станции')
    circle = models.ForeignKey(Circle, blank=True, null=True, on_delete=models.SET_NULL, verbose_name='Диспетчерский круг')
    shch = models.ForeignKey(SHCH, blank=True, null=True, on_delete=models.SET_NULL, verbose_name='Дистанция сигнализации и связи')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Станция'
        verbose_name_plural = 'Станции'

