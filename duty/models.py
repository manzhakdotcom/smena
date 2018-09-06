from django.db import models

from staff.models import Employee

# Create your models here.


class Duty(models.Model):
    date = models.DateTimeField(verbose_name='Дата дежурства')


class DutyStaff(models.Model):
    duty = models.OneToOneField(
        Duty,
        primary_key=True,
        on_delete=models.CASCADE,
    )
    employee = models.ForeignKey(
        Employee,
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
