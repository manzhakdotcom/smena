from django.db import models

# Create your models here.


class Organization(models.Model):
    name = models.CharField(max_length=128, verbose_name='Название организации')
    abbr = models.CharField(max_length=128, verbose_name='Аббревиатура')

    def __str__(self):
        return self.abbr

    class Meta:
        verbose_name = 'Организация'
        verbose_name_plural = 'Организации'


class Position(models.Model):
    name = models.CharField(max_length=128, verbose_name='Должность')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'


class Employee(models.Model):
    surname = models.CharField(max_length=128, verbose_name='Фамилия')
    name = models.CharField(max_length=128, verbose_name='Имя')
    patronymic = models.CharField(max_length=128, verbose_name='Отчество')
    position = models.ForeignKey(Position, blank=True, null=True, on_delete=models.SET_NULL, verbose_name='Должность')
    organization = models.ForeignKey(Organization, blank=True, null=True, on_delete=models.SET_NULL, verbose_name='Организация')

    def __str__(self):
        return self.surname

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'