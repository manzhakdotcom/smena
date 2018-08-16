from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hello_world(request):
    return HttpResponse('Hello World!')

def index(request, val):
    if request.method == 'GET':
        return render(request, 'index.html', {'val': val})