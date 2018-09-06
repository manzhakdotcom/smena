import ast

from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone

from duty.forms import DutyForm
from duty.models import Duty


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
            duty_employees = {}
            for field in form:
                duty_employees.update({field.html_name: field.data})
            duty = Duty(date=timezone.now(), duty_employees=duty_employees)
            duty.save()
            return render(request, 'staff/index.html')
        else:
            data = {
                'form': form
            }
            return render(request, 'duty/form.html', data)
    return HttpResponse(status=405)


def detail(request):
    if request.method == 'GET':
        duty = Duty.objects.all()[0]
        employees = ast.literal_eval(duty.duty_employees)
        data = {
            'dutys': Duty.objects.all()[0]
        }
        return render(request, 'duty/detail.html', data)
    return HttpResponse(status=405)