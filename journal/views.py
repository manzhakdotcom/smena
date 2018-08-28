from django.urls import reverse
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.utils import timezone

from journal.models import WriteDown, WriteOut, ExtraWriteOut
from journal.forms import WriteOutForm, WriteDownForm, ExtraWriteOutForm


# Create your views here.
def index(request):
    if request.method == 'GET':
        all_write_down = WriteDown.objects.all()
        date = timezone.now
        data = {
            'alert': request.GET.get('alert', False),
            'date': date,
            'all_write_down': all_write_down,
        }
        return render(request, 'index.html', data)
    return HttpResponse(status=405)


def detail(request, write_down_id):
    if request.method == 'GET':
        date = timezone.now
        data = {
            'date': date,
            'write_down': WriteDown.objects.get(id=write_down_id),
            'write_out': WriteOut.objects.filter(write_down_id=write_down_id).first(),
            'extra_write_out': ExtraWriteOut.objects.filter(write_down_id=write_down_id).first(),
        }
        return render(request, 'journal/detail.html', data)
    return HttpResponse(status=405)


def write_down(request):
    if request.method == 'GET':
        form = WriteDownForm()
        return render(request, 'journal/add/write-down.html', {'form': form})


def write_out(request, write_down_id):
    if request.method == 'GET':
        write_down = WriteDown.objects.select_related().filter(id=write_down_id).first()

        if not write_down:
            return HttpResponseRedirect('{}?alert=write_down_no'.format(reverse('index')))

        form = WriteOutForm()
        data = {
            'write_down': write_down,
            'form': form
        }
        return render(request, 'journal/add/write-out.html', data)
    return HttpResponse(status=405)


def extra_write_out(request, write_down_id):
    if request.method == 'GET':
        form = ExtraWriteOutForm()
        data = {
            'write_down_id': write_down_id,
            'form': form
        }
        return render(request, 'journal/add/extra-write-out.html', data)
