from django.urls import reverse
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone

from journal.models import WriteDown, WriteOut, ExtraWriteOut
from journal.forms import WriteOutForm, WriteDownForm, ExtraWriteOutForm
from journal.utils import set_properties_to_write_down, get_duty_time


# Create your views here.
def index(request):
    if request.method == 'GET':
        all_write_down = set_properties_to_write_down()
        data = {
            'alert': request.GET.get('alert', False),
            'duty_time': get_duty_time(),
            'all_write_down': all_write_down,
        }
        return render(request, 'index.html', data)
    return HttpResponse(status=405)


def detail(request, write_down_id):
    if request.method == 'GET':
        data = {
            'write_down': WriteDown.objects.get(id=write_down_id),
            'write_out': WriteOut.objects.filter(write_down_id=write_down_id).first(),
            'extra_write_out': ExtraWriteOut.objects.filter(write_down_id=write_down_id).first(),
        }
        return render(request, 'journal/detail.html', data)
    return HttpResponse(status=405)


def write_down(request):
    if request.method == 'GET':
        form = WriteDownForm()
        data = {
            'form': form
        }
        return render(request, 'journal/add/write-down.html', data)
    elif request.method == 'POST':
        form = WriteDownForm(request.POST)
        if form.is_valid():
            write_down = form.save()
            return HttpResponseRedirect(reverse('journal:detail', kwargs={'write_down_id': write_down.pk}))
        else:
            data = {
                'form': form
            }
            return render(request, 'journal/add/write-down.html', data)
    return HttpResponse(status=405)


def write_out(request, write_down_id):
    write_down = WriteDown.objects.select_related().filter(id=write_down_id).first()
    if not write_down:
        return HttpResponseRedirect('{}?alert=write_down_no'.format(reverse('index')))
    if request.method == 'GET':
        form = WriteOutForm(initial={
            'write_down': write_down
        })
        data = {
            'write_down': write_down,
            'form': form
        }
        return render(request, 'journal/add/write-out.html', data)
    elif request.method == 'POST':
        form = WriteOutForm(request.POST)
        if form.is_valid():
            write_out = form.save()
            return HttpResponseRedirect(reverse('journal:detail', kwargs={'write_down_id': request.POST['write_down']}))
        else:
            data = {
                'write_down': write_down,
                'form': form
            }
            return render(request, 'journal/add/write-out.html', data)
    
    return HttpResponse(status=405)


def extra_write_out(request, write_down_id):
    write_down = WriteDown.objects.select_related().filter(id=write_down_id).first()
    if not write_down:
        return HttpResponseRedirect('{}?alert=write_down_no'.format(reverse('index')))
    if request.method == 'GET':
        form = ExtraWriteOutForm(initial={
            'write_down': write_down
        })
        data = {
            'write_down': write_down,
            'form': form
        }
        return render(request, 'journal/add/extra-write-out.html', data)
    elif request.method == 'POST':
        form = ExtraWriteOutForm(request.POST)
        if form.is_valid():
            extra_write_out = form.save()
            return HttpResponseRedirect(reverse('journal:detail', kwargs={'write_down_id': request.POST['write_down']}))
        else:
            data = {
                'write_down': write_down,
                'form': form
            }
            return render(request, 'journal/add/extra-write-out.html', data)
    
    return HttpResponse(status=405)
