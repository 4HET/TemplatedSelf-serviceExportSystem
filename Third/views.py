import traceback
from datetime import datetime

import docxtpl
import docx
from django.http import StreamingHttpResponse, HttpResponse
from django.shortcuts import render, redirect
from django.utils.encoding import escape_uri_path
from docx import Document
from docx.shared import Cm
from docxcompose.composer import Composer
from docxtpl import DocxTemplate
from Register.models import User
from docx.shared import Mm
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
    # 法定代表人名称
    fddbrmc = request.COOKIES.get('fddbrmc')
    # 被授权人姓名及身份证代码
    xmjsfzdm = request.COOKIES.get('xmjsfzdm')
    # 被授权人电话
    bsqrdh = request.COOKIES.get('bsqrdh')
    pay = request.COOKIES.get('pay')
    wordPay = request.COOKIES.get('wordPay')
    tm = request.COOKIES.get('time')
    print(phone)

    # 日期
    year = datetime.now().year
    month = datetime.now().month
    day = datetime.now().day
    document = Document(r"./statics/docx/temp.docx")
    replace_dict = {
        # 项目名称
        "purchaseDemandName": projectName,
        # 项目编号
        "businessId": projectNumber,
        # 供应商名称
        "UserName": SupplierName,
        # 联系电话
        "personTel": phone,
        # 联系地址
        "lxdz": address,
        # 电子函件/邮箱
        "email": email,
        # 日期
        "year": year,
        "month": month,
        "day": day,
        # 采购人名称
        "purchasing": bossName,
        # 供销商开户银行
        "qybank": sdk,
        # 账号
        "qyzh": sdan,
        # 法定代表人名称
        'fddbrmc': fddbrmc,
        # 被授权人姓名及身份证代码
        'xmjsfzdm': xmjsfzdm,
        # 被授权人电话
        'bsqrdh': bsqrdh,
        'pay': pay,
        'wordPay': wordPay,
        'time': tm,
    }

    document = check_and_change(document, replace_dict)
    filename = r"./statics/user/{}responseFile.docx".format(username)
    document.save(filename)

    source_file_path_list = [filename]
    document = Document(r"./statics/docx/temp_end.docx")

    temp_end = r"./statics/user/{}_temp_end.docx".format(username)
    document = check_and_change(document, replace_dict)
    document.save(temp_end)

    dt = request.COOKIES.get('detail')
    dv = request.COOKIES.get('deviate')
    ip = request.COOKIES.get('impl')
    if dt is not None:
        source_file_path_list.append(r"./tmp/{}".format(dt))
    source_file_path_list.append(temp_end)
    if dv is not None:
        source_file_path_list.append(r"./tmp/{}".format(dv))
    if ip is not None:
        source_file_path_list.append(r"./tmp/{}".format(ip))
    final_path = r"./tmp/{}_final.docx".format(username)
    merge_doc(source_file_path_list, final_path)
    print(final_path)

    rp = fr"./img/{username}.png"
    if not replace_picture(final_path, rp):
        print("=======picture========")
        return render(request, 'second.html')

    if not replace_sf(final_path, fr"./img/{username}_sf.png"):
        print("=======sf========")
        return render(request, 'second.html')

    def down_chunk_file_manager(file_path, chuck_size=1024):
        with open(file_path, "rb") as file:
            while True:
                chuck_stream = file.read(chuck_size)
                if chuck_stream:
                    yield chuck_stream
                else:
                    break

    docx_path = r"./statics/docx/fj.docx"
    target_path = r"./tmp/{}_fj.docx".format(username)
    if not add_f(username, docx_path, target_path):
        return render(request, 'second.html')

    merge_doc([final_path, target_path], final_path)

    response = StreamingHttpResponse(down_chunk_file_manager(final_path))
    response['Content-Type'] = 'application/octet-stream'
    the_file_name = "响应文件.docx"
    # response["Content-Disposition"] = "attachment; filename*=UTF-8''{}".format(escape_uri_path(filename))
    response["Content-Disposition"] = "attachment; filename*=UTF-8''{}".format(escape_uri_path(the_file_name))

    print(escape_uri_path(the_file_name))

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
    zcze = list.TotalAssets
    cyry = list.NumberOfEmployees
    yysr = list.AnnualOperatingIncome
    hangye = 'hhh'
    pay = request.COOKIES.get('pay')
    wordPay = request.COOKIES.get('wordPay')

    print(phone)

    # 日期
    year = datetime.now().year
    month = datetime.now().month
    day = datetime.now().day
    document = Document(r"./statics/docx/zxqy.docx")
    replace_dict = {
        # 项目名称
        "purchaseDemandName": projectName,
        # 项目编号
        "businessId": projectNumber,
        # 供应商名称
        "UserName": SupplierName,
        # 联系电话
        "personTel": phone,
        # 联系地址
        "lxdz": address,
        # 电子函件/邮箱
        "email": email,
        # 日期
        "year": year,
        "month": month,
        "day": day,
        # 采购人名称
        "purchasing": bossName,
        # 供销商开户银行
        "qybank": sdk,
        # 账号
        "qyzh": sdan,
        # 日期
        "bztime": "{}年{}月{}日".format(year, month, day),
        # 资产总额
        "zcze": zcze,
        # 从业人员
        "cyry": cyry,
        # 营业收入
        "yysr": yysr,
        # 小型企业
        "qylx": "小型企业",
        # 所属行业
        "hangye": hangye,
        'pay': pay,
        'wordPay': wordPay,
    }

    document = check_and_change(document, replace_dict)
    filename = r"./tmp/{}_zxqy.docx".format(username)
    document.save(filename)

    rp = fr"./img/{username}.png"
    if not replace_zxqy(filename, rp):
        return render(request, 'second.html')

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
    the_file_path = "中小企业声明函.docx"
    response["Content-Disposition"] = "attachment; filename*=UTF-8''{}".format(escape_uri_path(the_file_path))
    # response["Content-Disposition"] = "attachment; filename={}".format("生成文件.docx")
    print(escape_uri_path(the_file_path))

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


def merge_doc(source_file_path_list, target_file_path):
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
        if i == 0:
            continue
        # 填充分页符文档
        target_composer.append(page_break_doc)
        # 拼接文档内容
        f = source_file_path_list[i]
        target_composer.append(Document(f))
    # 保存目标文档
    target_composer.save(target_file_path)


def replace_picture(final_path, replace_img_path):
    tpl = DocxTemplate(final_path)
    try:
        if tpl:
            try:
                tpl.replace_pic("Picture 3", replace_img_path)
            except:
                print("3不存在")
            try:
                tpl.replace_pic("Picture 6", replace_img_path)
            except:
                print("6不存在")
            try:
                # tpl.replace_pic("Picture 9", replace_img_path)
                tpl.replace_pic("图片 9", replace_img_path)
            except:
                print("9不存在")
            try:
                tpl.replace_pic("图片 11", replace_img_path)
            except:
                print("11不存在")
            try:
                tpl.replace_pic("图片 12", replace_img_path)
            except:
                print("12不存在")
        tpl.save(final_path)
        return True
    except Exception as e:
        print(traceback.format_exc())
        return False


def replace_sf(final_path, replace_img_path):
    tpl = DocxTemplate(final_path)
    try:
        if tpl:
            tpl.replace_pic("Picture 1", replace_img_path)
            tpl.replace_pic("图片 2", replace_img_path)
        tpl.save(final_path)
        return True
    except Exception as e:
        print(traceback.format_exc())
        return False


def replace_zxqy(final_path, replace_img_path):
    tpl = DocxTemplate(final_path)
    try:
        if tpl:
            tpl.replace_pic("Picture 2", replace_img_path)
        tpl.save(final_path)
        return True
    except Exception as e:
        print(traceback.format_exc())
        return False

def add_f(username, docx_path, target_path):
    try:
        fzm = r"./img/{}_fzm.png".format(username)
        fbm = r"./img/{}_fbm.png".format(username)
        bzm = r"./img/{}_bzm.png".format(username)
        bbm = r"./img/{}_bbm.png".format(username)

        # 创建docx对象
        daily_docx = docxtpl.DocxTemplate(docx_path)

        # 创建2张图片对象
        insert_image1 = docxtpl.InlineImage(daily_docx, fzm, width=Mm(140))
        insert_image2 = docxtpl.InlineImage(daily_docx, fbm, width=Mm(140))
        insert_image3 = docxtpl.InlineImage(daily_docx, bzm, width=Mm(140))
        insert_image4 = docxtpl.InlineImage(daily_docx, bbm, width=Mm(140))

        # 渲染内容
        context = {
            "fzm": insert_image1,
            "fbm": insert_image2,
            "bzm": insert_image3,
            "bbm": insert_image4,
        }

        # 渲染docx
        daily_docx.render(context)
        # 保存docx
        daily_docx.save(target_path)
        return True
    except Exception as e:
        print(traceback.format_exc())
        return False
