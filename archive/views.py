from django.shortcuts import render
from django.http import HttpResponse

from archive.forms import ArchiveForm


# Create your views here.
def index(request):
    data = {}
    if request.method == 'GET':
        data['form'] = ArchiveForm()
        if request.GET.get('archive_from') and request.GET.get('archive_to'):
            data['from'] = request.GET['archive_from']
            data['to'] = request.GET['archive_to']
        return render(request, 'archive/index.html', data)
    return HttpResponse(status=405)

