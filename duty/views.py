from datetime import datetime

from django.contrib import messages
from django.shortcuts import render, redirect
from django.db import transaction
from django.http import HttpResponse

from duty.forms import DutyForm
from duty.models import Duty, DutyStaff
from staff.models import Employee, Workplace
from . import DisplayMessages


# Create your views here.
def form(request):
    data = {
        'form': DutyForm()
    }
    if request.method == 'GET':
        return render(request, 'duty/form.html', data)
    elif request.method == 'POST':
        form = DutyForm(request.POST)
        if form.is_valid():
            with transaction.atomic():
                duty = Duty(date=datetime.now())
                duty.save()
                for key, value in form.cleaned_data.items():
                    employee = Employee.objects.get(id=value.pk)
                    workplace = Workplace.objects.get(id=int(key))
                    duty_staff = DutyStaff(duty=duty, employee=employee, workplace=workplace)
                    duty_staff.save()
            messages.success(request, DisplayMessages.DUTY_SAVE)
            return redirect('index')
        else:
            return render(request, 'duty/form.html', data)
    return HttpResponse(status=405)

