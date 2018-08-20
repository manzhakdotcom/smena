from django.shortcuts import render
from django.views.generic import View
from journal.forms import WriteOutForm
from django.contrib import messages


# Create your views here.
def index(request):
    if request.method == 'GET':
        return render(request, 'index.html', {})


def content(request, val):
    if request.method == 'GET':
        return render(request, 'content.html', {'val': val})


def add(request):
    if request.method == 'GET':
        return render(request, 'journal/add/index.html', {})


def write_down(request):
    if request.method == 'GET':
        return render(request, 'journal/add/write-down.html', {})


class WriteOut(View):

    def get(self, request):
        form = WriteOutForm()
        return render(request, 'journal/add/write-out.html', {'form': form})

    def post(self, request):
        form = WriteOutForm(data=request.POST)
        if form.is_valid():
            messages.success(request, form.cleaned_data['dispatcher'])
        else:
            messages.error(request, 'Validation failed')
        return render(request, 'journal/add/write-out.html', {'form': form})


def extra_write_out(request):
    if request.method == 'GET':
        return render(request, 'journal/add/extra-write-out.html', {})
