from django.shortcuts import render
from django.http import HttpResponse
from django.template.response import TemplateResponse

from archive.forms import ArchiveForm
from archive.utils import get_all_write_down


# Create your views here.
def index(request):
    ctx = {
        'form': ArchiveForm(),
        'date_from': None,
        'date_to': None,
        'items': (),
        }
    if 'archive_from' and 'archive_to' in request.GET:
        ctx['date_from'] = request.GET['archive_from']
        ctx['date_to'] = request.GET['archive_to']
        ctx['items'] = get_all_write_down(request.GET['archive_from'], request.GET['archive_to'])
    return TemplateResponse(request, 'archive/index.html', ctx)

