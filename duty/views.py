from django.shortcuts import render
from django.db import transaction
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone

from duty.forms import DutyForm
from duty.models import Duty, DutyStaff
from staff.models import Employee, Workplace


# Create your views here.
def index(request):
    if request.method == 'GET':
        data = {
            'form': DutyForm()
        }
        return render(request, 'duty/form.html', data)
    elif request.method == 'POST':
        form = DutyForm(request.POST)
        if form.is_valid():
            with transaction.atomic():
                duty = Duty(date=timezone.now())
                duty.save()
                for key, value in form.cleaned_data.items():
                    employee = Employee.objects.get(id=value.pk)
                    workplace = Workplace.objects.get(id=int(key))
                    duty_staff = DutyStaff(duty=duty, employee=employee, workplace=workplace)
                    duty_staff.save()
            return HttpResponseRedirect('/')
        else:
            data = {
                'form': form
            }
            return render(request, 'duty/form.html', data)
    return HttpResponse(status=405)


def detail(request):
    if request.method == 'GET':
        duty = Duty.objects.all().last()
        duty_staff = DutyStaff.objects.filter(duty=duty.pk)
        data = {
            'employees': duty_staff,
        }
        return render(request, 'duty/detail.html', data)
    return HttpResponse(status=405)
