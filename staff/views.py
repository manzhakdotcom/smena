from django.shortcuts import render
from django.http import HttpResponse

from staff.models import Employee
# Create your views here.


def index(request):
    if request.method == 'GET':
        data = {
            'employees': Employee.objects.all().order_by('organization__abbr', 'surname')
        }
        return render(request, 'staff/index.html', data)
    return HttpResponse(status=405)
