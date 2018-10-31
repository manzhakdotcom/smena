from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    data = {}
    if request.method == 'GET':
        if request.GET.get('from') and request.GET.get('to'):
            data = {
                'from': request.GET['from'],
                'to': request.GET['to']
            }
        return render(request, 'archive/index.html', data)
    return HttpResponse(status=405)

