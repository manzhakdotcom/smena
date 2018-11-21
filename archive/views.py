from django.shortcuts import render
from django.http import HttpResponse
from django.template.response import TemplateResponse

from archive.forms import ArchiveForm
from archive.utils import get_all_write_down


# Create your views here.
def index(request):
    if request.method == 'GET':
        ctx = {
            'form': ArchiveForm(),
            'date_from': None,
            'date_to': None,
            'all_write_down': (),
            }
        if 'archive_from' and 'archive_to' in request.GET:
            ctx['form'] = ArchiveForm(request.GET, initial={'archive_from': request.GET['archive_from'], 'archive_to': request.GET['archive_to']})
            ctx['date_from'] = request.GET['archive_from']
            ctx['date_to'] = request.GET['archive_to']
            ctx['all_write_down'] = get_all_write_down(request.GET['archive_from'], request.GET['archive_to'])
        return TemplateResponse(request, 'archive/index.html', ctx)
    return HttpResponse(status=405)

