from django.urls import reverse
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages

from journal.models import WriteDown, WriteOut, ExtraWriteOut
from journal.forms import WriteOutForm, WriteDownForm, ExtraWriteOutForm
from journal.utils import get_all_write_down, is_write_out, is_extra_write_out
from . import DisplayMessages


# Create your views here.
def index(request):
    if request.method == 'GET':
        data = {
            'alert': request.GET.get('alert', False),
            'all_write_down': get_all_write_down(),
        }
        return render(request, 'index.html', data)
    return HttpResponse(status=405)


def detail(request, write_down_id):
    try:
        write_down = WriteDown.objects.get(id=write_down_id)
    except WriteDown.DoesNotExist:
        messages.error(request, DisplayMessages.WRITE_DOWN_NOT_EXIST)
        return redirect('index')
    if request.method == 'GET':
        data = {
            'write_down': write_down,
            'write_out': WriteOut.objects.filter(write_down_id=write_down_id).first(),
            'extra_write_out': ExtraWriteOut.objects.filter(write_down_id=write_down_id).first(),
        }
        return render(request, 'journal/detail.html', data)
    return HttpResponse(status=405)


def write_down(request):
    if request.method == 'GET':
        form = WriteDownForm()
        data = {'form': form}
        return render(request, 'journal/add/write-down.html', data)
    elif request.method == 'POST':
        form = WriteDownForm(request.POST)
        if form.is_valid():
            write_down = form.save()
            messages.success(request, DisplayMessages.WRITE_DOWN_SAVE)
            return HttpResponseRedirect(reverse('journal:detail', kwargs={'write_down_id': write_down.pk}))
        else:
            data = {'form': form}
            return render(request, 'journal/add/write-down.html', data)
    return HttpResponse(status=405)


def write_out(request, write_down_id):
    try:
        write_down = WriteDown.objects.get(id=write_down_id)
    except WriteDown.DoesNotExist:
        messages.error(request, DisplayMessages.WRITE_DOWN_NOT_EXIST)
        return redirect('index')
    if is_write_out(write_down_id):
        messages.error(request, DisplayMessages.WRITE_OUT_IS)
        return redirect('index')
    data = {
        'write_down': write_down,
        'form': WriteOutForm(initial={'write_down': write_down})
    }
    if request.method == 'GET':
        return render(request, 'journal/add/write-out.html', data)
    elif request.method == 'POST':
        form = WriteOutForm(request.POST)
        if form.is_valid():
            write_out = form.save()
            messages.success(request, DisplayMessages.WRITE_OUT_SAVE)
            return HttpResponseRedirect(reverse('journal:detail', kwargs={'write_down_id': request.POST['write_down']}))
        else:
            return render(request, 'journal/add/write-out.html', data)
    
    return HttpResponse(status=405)


def extra_write_out(request, write_down_id):
    try:
        write_down = WriteDown.objects.get(id=write_down_id)
    except WriteDown.DoesNotExist:
        messages.error(request, DisplayMessages.WRITE_DOWN_NOT_EXIST)
        return redirect('index')
    if is_extra_write_out(write_down_id):
        messages.error(request, DisplayMessages.EXTRA_WRITE_OUT_IS)
        return redirect('index')
    data = {
        'write_down': write_down,
        'form': ExtraWriteOutForm(initial={'write_down': write_down})
    }
    if request.method == 'GET':
        return render(request, 'journal/add/extra-write-out.html', data)
    elif request.method == 'POST':
        form = ExtraWriteOutForm(request.POST)
        if form.is_valid():
            extra_write_out = form.save()
            messages.success(request, DisplayMessages.EXTRA_WRITE_OUT_SAVE)
            return HttpResponseRedirect(reverse('journal:detail', kwargs={'write_down_id': request.POST['write_down']}))
        else:
            return render(request, 'journal/add/extra-write-out.html', data)
    
    return HttpResponse(status=405)
