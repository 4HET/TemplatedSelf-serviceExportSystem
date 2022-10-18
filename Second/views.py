import os
import traceback

from django.http import HttpResponse, StreamingHttpResponse
from django.shortcuts import render, redirect
from django.utils.encoding import escape_uri_path
from docxtpl import DocxTemplate

from Second.forms import UploadFileForm, FileFieldForm
from Second.models import IMG, SF, Bsqr


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

def officialSeal(request):
    status = request.COOKIES.get('is_login')
    username = request.COOKIES.get('username')
    if not status:
        return redirect('/login/')
    img = IMG.objects.filter(username=username)
    # if img.count() != 0:
    #     return redirect('/showImg/')
    if request.method == 'POST':
        if img.count() != 0:
            img = IMG.objects.get(username=username)
            img.img = request.FILES.get('img')
            img.name = request.FILES.get('img').name
            img.img.name = username + '.png'
            if os.path.exists("./img/"+username + '.png'):
                os.remove("./img/"+username + '.png')
            print(img.img.url)
            img.save()
        else:
            img = request.FILES.get('img'),
            name = request.FILES.get('img').name
            print(img)

            new_img = IMG(
                img=request.FILES.get('img'),
                # name=name,
                name=request.FILES.get('img').name,
                username=request.COOKIES.get('username')
            )
            new_img.save()

            img = IMG.objects.get(username=username)
            img.img = request.FILES.get('img')
            img.name = request.FILES.get('img').name
            img.img.name = username + '.png'
            print(img.img.url)
            img.save()
        form = UploadFileForm()
        # return HttpResponse("<p>数据添加成功！</p>")
        return render(request, 'second.html', {'form': form})
    else:
        form = UploadFileForm()
    return render(request, 'second.html', {'form': form})

def sfSeal(request):
    status = request.COOKIES.get('is_login')
    username = request.COOKIES.get('username')
    if not status:
        return redirect('/login/')
    img = SF.objects.filter(username=username)
    # if img.count() != 0:
    #     return redirect('/showImg/')
    if request.method == 'POST':
        if img.count() != 0:
            img = SF.objects.get(username=username)
            img.img = request.FILES.get('img')
            img.name = request.FILES.get('img').name
            img.img.name = username + '_sf.png'
            if os.path.exists("./img/"+username + '_sf.png'):
                os.remove("./img/"+username + '_sf.png')
            print(img.img.url)
            img.save()
        else:
            img = request.FILES.get('img'),
            name = request.FILES.get('img').name
            print(img)

            new_img = SF(
                img=request.FILES.get('img'),
                name=request.FILES.get('img').name,
                username=request.COOKIES.get('username')
            )
            new_img.save()

            img = SF.objects.get(username=username)
            img.img = request.FILES.get('img')
            img.name = request.FILES.get('img').name
            img.img.name = username + '_sf.png'
            if os.path.exists(username + '_sf.png'):
                os.remove(username + '_sf.png')
            print(img.img.url)
            print("not exists!")
            img.save()
        form = UploadFileForm()
        # return HttpResponse("<p>数据添加成功！</p>")
        return render(request, 'second.html', {'form': form})
    else:
        form = UploadFileForm()
    return render(request, 'second.html', {'form': form})

def bsqr(request):
    status = request.COOKIES.get('is_login')
    username = request.COOKIES.get('username')
    if not status:
        return redirect('/login/')
    img = Bsqr.objects.filter(username=username)
    # if img.count() != 0:
    #     return redirect('/showImg/')
    if request.method == 'POST':
        if img.count() != 0:
            img = Bsqr.objects.get(username=username)
            img.img = request.FILES.get('img')
            img.name = request.FILES.get('img').name
            img.img.name = username + '_bsqr.png'
            if os.path.exists("./img/"+username + '_bsqr.png'):
                os.remove("./img/"+username + '_bsqr.png')
            print(img.img.url)
            img.save()
        else:
            img = request.FILES.get('img'),
            name = request.FILES.get('img').name
            print(img)

            new_img = Bsqr(
                img=request.FILES.get('img'),
                # name=name,
                name=request.FILES.get('img').name,
                username=request.COOKIES.get('username')
            )
            new_img.save()

            img = Bsqr.objects.get(username=username)
            img.img = request.FILES.get('img')
            img.name = request.FILES.get('img').name
            img.img.name = username + '_bsqr.png'
            print(img.img.url)
            img.save()
        form = UploadFileForm()
        # return HttpResponse("<p>数据添加成功！</p>")
        return render(request, 'second.html', {'form': form})
    else:
        form = UploadFileForm()
    return render(request, 'second.html', {'form': form})
def fzm(request):
    status = request.COOKIES.get('is_login')
    username = request.COOKIES.get('username')
    if not status:
        return redirect('/login/')
    img = Bsqr.objects.filter(username=username)
    # if img.count() != 0:
    #     return redirect('/showImg/')
    if request.method == 'POST':
        if img.count() != 0:
            img = Bsqr.objects.get(username=username)
            img.img = request.FILES.get('img')
            img.name = request.FILES.get('img').name
            img.img.name = username + '_fzm.png'
            if os.path.exists("./img/"+username + '_fzm.png'):
                os.remove("./img/"+username + '_fzm.png')
            print(img.img.url)
            img.save()
        else:
            img = request.FILES.get('img'),
            name = request.FILES.get('img').name
            print(img)

            new_img = Bsqr(
                img=request.FILES.get('img'),
                # name=name,
                name=request.FILES.get('img').name,
                username=request.COOKIES.get('username')
            )
            new_img.save()

            img = Bsqr.objects.get(username=username)
            img.img = request.FILES.get('img')
            img.name = request.FILES.get('img').name
            img.img.name = username + '_fzm.png'
            print(img.img.url)
            img.save()
        form = UploadFileForm()
        # return HttpResponse("<p>数据添加成功！</p>")
        return render(request, 'second.html', {'form': form})
    else:
        form = UploadFileForm()
    return render(request, 'second.html', {'form': form})
def fbm(request):
    status = request.COOKIES.get('is_login')
    username = request.COOKIES.get('username')
    if not status:
        return redirect('/login/')
    img = Bsqr.objects.filter(username=username)
    # if img.count() != 0:
    #     return redirect('/showImg/')
    if request.method == 'POST':
        if img.count() != 0:
            img = Bsqr.objects.get(username=username)
            img.img = request.FILES.get('img')
            img.name = request.FILES.get('img').name
            img.img.name = username + '_fbm.png'
            if os.path.exists("./img/"+username + '_fbm.png'):
                os.remove("./img/"+username + '_fbm.png')
            print(img.img.url)
            img.save()
        else:
            img = request.FILES.get('img'),
            name = request.FILES.get('img').name
            print(img)

            new_img = Bsqr(
                img=request.FILES.get('img'),
                # name=name,
                name=request.FILES.get('img').name,
                username=request.COOKIES.get('username')
            )
            new_img.save()

            img = Bsqr.objects.get(username=username)
            img.img = request.FILES.get('img')
            img.name = request.FILES.get('img').name
            img.img.name = username + '_fbm.png'
            print(img.img.url)
            img.save()
        form = UploadFileForm()
        # return HttpResponse("<p>数据添加成功！</p>")
        return render(request, 'second.html', {'form': form})
    else:
        form = UploadFileForm()
    return render(request, 'second.html', {'form': form})
def bzm(request):
    status = request.COOKIES.get('is_login')
    username = request.COOKIES.get('username')
    if not status:
        return redirect('/login/')
    img = Bsqr.objects.filter(username=username)
    # if img.count() != 0:
    #     return redirect('/showImg/')
    if request.method == 'POST':
        if img.count() != 0:
            img = Bsqr.objects.get(username=username)
            img.img = request.FILES.get('img')
            img.name = request.FILES.get('img').name
            img.img.name = username + '_bzm.png'
            if os.path.exists("./img/"+username + '_bzm.png'):
                os.remove("./img/"+username + '_bzm.png')
            print(img.img.url)
            img.save()
        else:
            img = request.FILES.get('img')
            name = request.FILES.get('img').name
            print(img)

            new_img = Bsqr(
                img=request.FILES.get('img'),
                # name=name,
                name=request.FILES.get('img').name,
                username=request.COOKIES.get('username')
            )
            new_img.save()

            img = Bsqr.objects.get(username=username)
            img.img = request.FILES.get('img')
            img.name = request.FILES.get('img').name
            img.img.name = username + '_bzm.png'
            print(img.img.url)
            img.save()
        form = UploadFileForm()
        # return HttpResponse("<p>数据添加成功！</p>")
        return render(request, 'second.html', {'form': form})
    else:
        form = UploadFileForm()
    return render(request, 'second.html', {'form': form})
def bbm(request):
    status = request.COOKIES.get('is_login')
    username = request.COOKIES.get('username')
    if not status:
        return redirect('/login/')
    img = Bsqr.objects.filter(username=username)
    # if img.count() != 0:
    #     return redirect('/showImg/')
    if request.method == 'POST':
        if img.count() != 0:
            img = Bsqr.objects.get(username=username)
            img.img = request.FILES.get('img')
            img.name = request.FILES.get('img').name
            img.img.name = username + '_bbm.png'
            if os.path.exists("./img/"+username + '_bbm.png'):
                os.remove("./img/"+username + '_bbm.png')
            print(img.img.url)
            img.save()
        else:
            img = request.FILES.get('img'),
            name = request.FILES.get('img').name
            print(img)

            new_img = Bsqr(
                img=request.FILES.get('img'),
                # name=name,
                name=request.FILES.get('img').name,
                username=request.COOKIES.get('username')
            )
            new_img.save()

            img = Bsqr.objects.get(username=username)
            img.img = request.FILES.get('img')
            img.name = request.FILES.get('img').name
            img.img.name = username + '_card.png'
            print(img.img.url)
            img.save()
        form = UploadFileForm()
        # return HttpResponse("<p>数据添加成功！</p>")
        return render(request, 'second.html', {'form': form})
    else:
        form = UploadFileForm()
    return render(request, 'second.html', {'form': form})

def solve_docx_detail(source_path, target_path, gongzhang, rq):
    tpl = DocxTemplate(source_path)
    touming = r"./img/touming.png"
    if tpl:
        try:
            if not os.path.exists(gongzhang):
                gongzhang = touming
            tpl.replace_pic("Picture 12", gongzhang)

            context = {
                "bzrq": rq,
            }
            tpl.render(context)
            tpl.save(target_path)
        except Exception as e:
            print(traceback.format_exc())
def solve_docx_deviate(source_path, target_path, gongzhang):
    tpl = DocxTemplate(source_path)
    touming = r"./img/touming.png"
    if tpl:
        try:
            if not os.path.exists(gongzhang):
                gongzhang = touming
            tpl.replace_pic("Picture 1", gongzhang)


            tpl.save(target_path)
        except Exception as e:
            print(traceback.format_exc())
def solve_docx_impl(source_path, target_path, gongzhang):
    tpl = DocxTemplate(source_path)
    touming = r"./img/touming.png"

    if tpl:
        try:
            if not os.path.exists(gongzhang):
                gongzhang = touming
            tpl.replace_pic("Picture 15", gongzhang)


            tpl.save(target_path)
        except Exception as e:
            print(traceback.format_exc())

def check_and_change(document, replace_dict):
    """
    遍历word中的所有 paragraphs，在每一段中发现含有key 的内容，就替换为 value 。
   （key 和 value 都是replace_dict中的键值对。）
    """
    for para in document.paragraphs:
        for i in range(len(para.runs)):
            for key, value in replace_dict.items():
                if key in para.runs[i].text:
                    print(str(key) + "->" + str(value))
                    print(str(value))
                    para.runs[i].text = para.runs[i].text.replace(str(key), str(value))
    return document

def downloadDetail(request):
    filename = r"./statics/docx/detail.docx"
    username = request.COOKIES.get('username')
    gongzhang = r"./img/{}_gz.png".format(username)

    rq = request.COOKIES.get('bzrq')

    target_name = r"./tmp/{}.detail.docx".format(username)

    solve_docx_detail(filename, target_name, gongzhang, rq)

    def down_chunk_file_manager(file_path, chuck_size=1024):
        with open(file_path, "rb") as file:
            while True:
                chuck_stream = file.read(chuck_size)
                if chuck_stream:
                    yield chuck_stream
                else:
                    break

    response = StreamingHttpResponse(down_chunk_file_manager(target_name))
    response['Content-Type'] = 'application/octet-stream'
    the_file_name = "明细表模板.docx"
    response["Content-Disposition"] = "attachment; filename*=UTF-8''{}".format(escape_uri_path(the_file_name))


    return response

def downloadDevite(request):
    filename = r"./statics/docx/deviate.docx"
    username = request.COOKIES.get('username')
    gongzhang = r"./img/{}_gz.png".format(username)

    target_name = r"./tmp/{}.devite.docx".format(username)

    solve_docx_deviate(filename, target_name, gongzhang)

    def down_chunk_file_manager(file_path, chuck_size=1024):
        with open(file_path, "rb") as file:
            while True:
                chuck_stream = file.read(chuck_size)
                if chuck_stream:
                    yield chuck_stream
                else:
                    break

    response = StreamingHttpResponse(down_chunk_file_manager(target_name))
    response['Content-Type'] = 'application/octet-stream'
    the_file_name = "技术偏离表模板.docx"
    response["Content-Disposition"] = "attachment; filename*=UTF-8''{}".format(escape_uri_path(the_file_name))
    return response

def downloadImpl(request):
    filename = r"./statics/docx/impl.docx"
    username = request.COOKIES.get('username')
    gongzhang = r"./img/{}_gz.png".format(username)

    target_name = r"./tmp/{}.impl.docx".format(username)

    solve_docx_impl(filename, target_name, gongzhang)

    def down_chunk_file_manager(file_path, chuck_size=1024):
        with open(file_path, "rb") as file:
            while True:
                chuck_stream = file.read(chuck_size)
                if chuck_stream:
                    yield chuck_stream
                else:
                    break

    response = StreamingHttpResponse(down_chunk_file_manager(target_name))
    response['Content-Type'] = 'application/octet-stream'
    the_file_name = "项目实施方案模板.docx"
    response["Content-Disposition"] = "attachment; filename*=UTF-8''{}".format(escape_uri_path(the_file_name))
    return response


