from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    if request.method == 'GET':
        return render(request, 'index.html', {})


def content(request, val):
    if request.method == 'GET':
        return render(request, 'content.html', {'val': val})


def add(request):
    if request.method == 'GET':
        return render(request, 'add/index.html', {}) 


def write_down(request):
    if request.method == 'GET':
        return render(request, 'add/write-down.html', {})  


def write_out(request):
    if request.method == 'GET':
        return render(request, 'add/write-out.html', {})


def extra_write_out(request):
    if request.method == 'GET':
        return render(request, 'add/extra-write-out.html', {})
