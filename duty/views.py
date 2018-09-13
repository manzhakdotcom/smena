from datetime import datetime

from django.urls import reverse
from django.shortcuts import render
from django.db import transaction
from django.http import HttpResponse, HttpResponseRedirect

from duty.forms import DutyForm
from duty.models import Duty, DutyStaff
from staff.models import Employee, Workplace


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
            return HttpResponseRedirect('{}?alert=duty_added'.format(reverse('index')))
        else:
            return render(request, 'duty/form.html', data)
    return HttpResponse(status=405)

