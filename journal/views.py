from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.utils import timezone

from journal.models import WriteDown, WriteOut, ExtraWriteOut
from journal.forms import WriteOutForm, WriteDownForm, ExtraWriteOutForm


# Create your views here.
def index(request):
    if request.method == 'GET':
        all_write_down = WriteDown.objects.all()
        date = timezone.now
        data = {
            'date': date,
            'items': all_write_down,
        }
        return render(request, 'index.html', data)
    return HttpResponse(status=405)


def detail(request, id):
    if request.method == 'GET':
        date = timezone.now
        data = {
            'date': date,
            'write_down': WriteDown.objects.get(id=id),
            'write_out': WriteOut.objects.filter(write_down_id=id).first(),
            'extra_write_out': ExtraWriteOut.objects.filter(write_down_id=id).first(),
        }
        return render(request, 'journal/detail.html', data)


def write_down(request):
    if request.method == 'GET':
        form = WriteDownForm()
        return render(request, 'journal/add/write-down.html', {'form': form})


def write_out(request):
    if request.method == 'GET':
        form = WriteOutForm()
        data = {
            'form': form
        }
        return render(request, 'journal/add/write-out.html', data)


def extra_write_out(request):
    if request.method == 'GET':
        form = ExtraWriteOutForm()
        data = {
            'form': form
        }
        return render(request, 'journal/add/extra-write-out.html', data)
