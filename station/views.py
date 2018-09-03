from django.shortcuts import render
from django.http import HttpResponse

from station.models import Station


# Create your views here.
def index(request):
    if request.method == 'GET':
        data = {
            'stations': Station.objects.all().order_by('circle__name')
        }
        return render(request, 'station/index.html', data)
    return HttpResponse(status=405)
