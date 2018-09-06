from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
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
            duty = Duty(date=timezone.now(), duty_employees=form.cleaned_data)
            duty.save()
            return HttpResponseRedirect('/')
        else:
            data = {
                'form': form
            }
            return render(request, 'duty/form.html', data)
    return HttpResponse(status=405)


def detail(request):
    duty = Duty.objects.all().last()
    if request.method == 'GET':
        data = {
            'employees': duty.duty_employees,
        }
        return render(request, 'duty/detail.html', data)
    return HttpResponse(status=405)
