import os

from django.http import HttpResponse, StreamingHttpResponse
from django.shortcuts import render, redirect
from django.utils.encoding import escape_uri_path

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
    return render(request, 'third.html', {'form': form})
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

def handle_upload_file(file, name):
    with open("./tmp/%s" % name+'_'+file.name, 'wb+') as f:
        for chunk in file.chunks():
            f.write(chunk)
    return name+'_'+file.name

def detail(request):
    status = request.COOKIES.get('is_login')
    username = request.COOKIES.get('username')
    if not status:
        return redirect('/login/')
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            rep = render(request, 'second.html', {'form': form})
            dt = handle_upload_file(request.FILES['file'], username + '_detail')
            rep.set_cookie('detail', dt)
            return rep
    else:
        print('hhh')
        form = UploadFileForm()
    return render(request, 'second.html', {'form': form})


def deviate(request):
    status = request.COOKIES.get('is_login')
    username = request.COOKIES.get('username')
    if not status:
        return redirect('/login/')
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            dv = handle_upload_file(request.FILES['file'], username + '_deviate')
            rep = render(request, 'second.html', {'form': form})
            rep.set_cookie('deviate', dv)
            return rep
    else:
        print('hhh')
        form = UploadFileForm()
    return render(request, 'second.html', {'form': form})

def impl(request):
    status = request.COOKIES.get('is_login')
    username = request.COOKIES.get('username')
    if not status:
        return redirect('/login/')
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            rep = render(request, 'second.html', {'form': form})
            ip = handle_upload_file(request.FILES['file'], username + '_impl')
            rep.set_cookie('impl', ip)
            return rep
    else:
        print('hhh')
        form = UploadFileForm()
    return render(request, 'second.html', {'form': form})


def downloadDetail(request):
    filename = r".\statics\docx\detail.docx"

    def down_chunk_file_manager(file_path, chuck_size=1024):
        with open(file_path, "rb") as file:
            while True:
                chuck_stream = file.read(chuck_size)
                if chuck_stream:
                    yield chuck_stream
                else:
                    break

    response = StreamingHttpResponse(down_chunk_file_manager(filename))
    response['Content-Type'] = 'application/octet-stream'
    response["Content-Disposition"] = "attachment; filename*=UTF-8''{}".format(escape_uri_path(filename))


    return response

def downloadDevite(request):
    filename = r".\statics\docx\deviate.docx"

    def down_chunk_file_manager(file_path, chuck_size=1024):
        with open(file_path, "rb") as file:
            while True:
                chuck_stream = file.read(chuck_size)
                if chuck_stream:
                    yield chuck_stream
                else:
                    break

    response = StreamingHttpResponse(down_chunk_file_manager(filename))
    response['Content-Type'] = 'application/octet-stream'
    response["Content-Disposition"] = "attachment; filename*=UTF-8''{}".format(escape_uri_path(filename))


    return response

def downloadImpl(request):
    filename = r".\statics\docx\impl.docx"

    def down_chunk_file_manager(file_path, chuck_size=1024):
        with open(file_path, "rb") as file:
            while True:
                chuck_stream = file.read(chuck_size)
                if chuck_stream:
                    yield chuck_stream
                else:
                    break

    response = StreamingHttpResponse(down_chunk_file_manager(filename))
    response['Content-Type'] = 'application/octet-stream'
    response["Content-Disposition"] = "attachment; filename*=UTF-8''{}".format(escape_uri_path(filename))


    return response