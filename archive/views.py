from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    if request.method == 'GET':
        data = {}
        return render(request, 'archive/index.html', data)
    return HttpResponse(status=405)
