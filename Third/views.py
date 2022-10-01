from datetime import datetime

from django.http import StreamingHttpResponse, HttpResponse
from django.shortcuts import render, redirect
from django.utils.encoding import escape_uri_path
from docx import Document
from Register.models import User
import time


# Create your views here.
def third(request):
    ctx = {}
    status = request.COOKIES.get('is_login')
    if not status:
        return redirect('/login/')
    return render(request, 'third.html', ctx)


def responseFile(request):
    username = request.COOKIES.get('username')
    password = request.COOKIES.get('password')
    list = User.objects.filter(username=username, password=password).first()

    projectName = request.COOKIES.get('projectName')
    projectNumber = request.COOKIES.get('projectNumber')
    SupplierName = list.SupplierName
    bossName = request.COOKIES.get('bossName')
    phone = list.phone
    address = list.address
    email = list.email
    sdk = list.SupplierDepositBank
    sdan = list.SupplierCorporateAccountNumber
    print(phone)

    # 日期
    year = datetime.now().year
    month = datetime.now().month
    day = datetime.now().day
    document = Document(r".\statics\docx\temp.docx")
    replace_dict = {
        # 项目名称
        "projectName": projectName,
        # 项目编号
        "projectNumber": projectNumber,
        # 供应商名称
        "SupplierName": SupplierName,
        # 联系电话
        "phone": phone,
        # 联系地址
        "address": address,
        # 电子函件/邮箱
        "email": email,
        # 日期
        "year": year,
        "month": month,
        "day": day,
        # 采购人名称
        "bossName": bossName,
        # 供销商开户银行
        "sdk": sdk,
        # 账号
        "sdan": sdan,
    }

    document = check_and_change(document, replace_dict)
    filename = r".\statics\user\{}responseFile.docx".format(username)
    document.save(filename)

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

    return render(request, 'third.html', {})


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

def file_download(request):
    # do something...
    with open('file_name.txt') as f:
        c = f.read()
    return HttpResponse(c)