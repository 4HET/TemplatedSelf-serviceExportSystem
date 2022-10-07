from datetime import datetime

from django.http import StreamingHttpResponse, HttpResponse
from django.shortcuts import render, redirect
from django.utils.encoding import escape_uri_path
from docx import Document
from docxcompose.composer import Composer

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

    source_file_path_list = [filename]
    document = Document(r".\statics\docx\temp_end.docx")


    temp_end = r".\statics\user\{}_temp_end.docx".format(username)
    document = check_and_change(document, replace_dict)
    document.save(temp_end)


    dt = request.COOKIES.get('detail')
    dv = request.COOKIES.get('deviate')
    ip = request.COOKIES.get('impl')
    if dt is not None:
        source_file_path_list.append(r".\tmp\{}".format(dt))
    source_file_path_list.append(temp_end)
    if dv is not None:
        source_file_path_list.append(r".\tmp\{}".format(dv))
    if ip is not None:
        source_file_path_list.append(r".\tmp\{}".format(ip))



    final_path = r".\tmp\{}_final.docx".format(username)
    merge_doc(source_file_path_list, final_path)


    def down_chunk_file_manager(file_path, chuck_size=1024):
        with open(file_path, "rb") as file:
            while True:
                chuck_stream = file.read(chuck_size)
                if chuck_stream:
                    yield chuck_stream
                else:
                    break

    response = StreamingHttpResponse(down_chunk_file_manager(final_path))
    response['Content-Type'] = 'application/octet-stream'
    response["Content-Disposition"] = "attachment; filename*=UTF-8''{}".format(escape_uri_path(filename))
    print(escape_uri_path(filename))

    return response

def zxqy(request):
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
    document = Document(r".\statics\docx\zxqy.docx")
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
    filename = r".\tmp\{}_zxqy.docx".format(username)
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
    print(escape_uri_path(filename))

    return response

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

def merge_doc(source_file_path_list,target_file_path):
    '''
    合并多个docx文件
    :param source_file_path_list: 源文件路径列表
    :param target_file_path: 目标文件路径
    :return:
    '''
    # 填充分页符号文档
    page_break_doc = Document()
    page_break_doc.add_page_break()
    # 定义新文档
    target_doc = Document(source_file_path_list[0])
    target_composer = Composer(target_doc)
    for i in range(len(source_file_path_list)):

        # 跳过第一个作为模板的文件
        if i==0:
            continue
        # 填充分页符文档
        target_composer.append(page_break_doc)
        # 拼接文档内容
        f = source_file_path_list[i]
        target_composer.append(Document(f))
    # 保存目标文档
    target_composer.save(target_file_path)