from django.http import HttpResponse
from django.shortcuts import render

from Second.forms import UploadFileForm


# Create your views here.
def second(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_upload_file(request.FILES['file'])
            # handle_upload_file(form.files['file'])
            return HttpResponse('upload success!')
    else:
        form = UploadFileForm()
    return render(request, 'second.html', {'form': form})

def sendPostSecond(request):
    context = {}
    context['hello'] = 'Hello World!'
    return render(request, 'third.html', context)

def upload_detail(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_upload_file(request.FILES['file'])
            # handle_upload_file(form.files['file'])
            return HttpResponse('upload success!')
    else:
        form = UploadFileForm()
    return render(request, 'second.html', {'form': form})

def handle_upload_file(file):
    with open("/tmp/%s" % file.name, 'wb+') as f:
        for chunk in file.chunks():
            f.write(chunk)