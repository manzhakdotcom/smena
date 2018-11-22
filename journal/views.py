from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404
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


def edit_extra_write_out(request, extra_write_out_id):
    extra_write_out_list = ExtraWriteOut.objects.is_published()
    extra_write_out = get_object_or_404(extra_write_out_list, write_down=extra_write_out_id)
    if request.method == 'GET':
        write_down = get_object_or_404(WriteDown, pk=extra_write_out_id)
        data = {
            'write_down': write_down,
            'form': ExtraWriteOutForm(instance=extra_write_out)
        }
        return render(request, 'journal/edit/extra-write-out.html', data)
    elif request.method == 'POST':
        form = ExtraWriteOutForm(request.POST or None, instance=extra_write_out)
        if form.is_valid():
            extra_write_out = form.save()
            messages.success(request, DisplayMessages.EXTRA_WRITE_OUT_EDIT)
            return HttpResponseRedirect(reverse('journal:detail', kwargs={'write_down_id': request.POST['write_down']}))
    return HttpResponse(status=405)


def edit_write_out(request, write_out_id):
    write_out_list = WriteOut.objects.is_published()
    write_out = get_object_or_404(write_out_list, write_down=write_out_id)
    if request.method == 'GET':
        write_down = get_object_or_404(WriteDown, pk=write_out_id)
        data = {
            'write_down': write_down,
            'form': WriteOutForm(instance=write_out)
        }
        return render(request, 'journal/edit/write-out.html', data)
    elif request.method == 'POST':
        form = WriteOutForm(request.POST or None, instance=write_out)
        if form.is_valid():
            write_out = form.save()
            messages.success(request, DisplayMessages.WRITE_OUT_EDIT)
            return HttpResponseRedirect(reverse('journal:detail', kwargs={'write_down_id': request.POST['write_down']}))
    return HttpResponse(status=405)


def edit_write_down(request, write_down_id):
    write_down = get_object_or_404(WriteDown, pk=write_down_id)
    if request.method == 'GET':
        form = WriteDownForm(instance=write_down)
        data = {'form': form,
                'write_down': write_down,
                }
        return render(request, 'journal/edit/write-down.html', data)
    elif request.method == 'POST':
        form = WriteDownForm(request.POST or None, instance=write_down)
        if form.is_valid():
            write_down = form.save()
            messages.success(request, DisplayMessages.WRITE_DOWN_EDIT)
            return HttpResponseRedirect(reverse('journal:detail', kwargs={'write_down_id': write_down.pk}))
    return HttpResponse(status=405)
