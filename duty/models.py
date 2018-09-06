from django.db import models

from staff.models import Employee

# Create your models here.


class Duty(models.Model):
    date = models.DateTimeField(verbose_name='Дата дежурства')
    duty_employees = models.CharField(max_length=128, verbose_name='Дежурный персонал')
