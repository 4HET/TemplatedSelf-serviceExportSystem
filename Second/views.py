import os

from django.http import HttpResponse
from django.shortcuts import render, redirect

from Second.forms import UploadFileForm, FileFieldForm


# Create your views here.
def second(request):
    status = request.COOKIES.get('is_login')
    if not status:
        return redirect('/login/')
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_upload_file(request.FILES['file'])
            return render(request, 'third.html', {'form': form})
    else:
        print('hhh')
        form = UploadFileForm()
    return render(request, 'second.html', {'form': form})
    # if request.method == 'POST':
    #     form = FileFieldForm(request.POST, request.FILES)
    #     files = request.FILES.getlist('file_field')  # 获得多个文件上传进来的文件列表。
    #     if form.is_valid():  # 表单数据如果合法
    #         for f in files:
    #             handle_upload_file(f)  # 处理上传来的文件
    #         return HttpResponse('文件上传成功！')
    # else:
    #     form = FileFieldForm()
    # return render(request, 'second.html', {'form': form})

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
    with open("./tmp/%s" % file.name, 'wb+') as f:
        for chunk in file.chunks():
            f.write(chunk)