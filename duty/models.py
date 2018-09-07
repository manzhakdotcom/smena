from django.db import models

from staff.models import Employee, Workplace

# Create your models here.


class Duty(models.Model):
    date = models.DateTimeField()


class DutyStaff(models.Model):
    duty = models.ForeignKey(
        Duty,
        on_delete=models.CASCADE,
    )
    employee = models.ForeignKey(
        Employee,
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    workplace = models.ForeignKey(
        Workplace,
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
