import os.path

import docxtpl
from django.shortcuts import render, redirect

import shutil

from docx.shared import Mm
from docxtpl import DocxTemplate, InlineImage

from First.models import Yyzz_first


# Create your views here.
def first(request):
    ctx = {}
    status = request.COOKIES.get('is_login')

    if not status:
        return redirect('/login/')
    if request.method == 'POST':
        username = request.COOKIES.get('username')
        # 项目名称
        projectName = request.POST['projectName']
        print(projectName)
        # 项目编号
        projectNumber = request.POST['projectNumber']
        # 采购人名称
        bossName = request.POST['bossName']
        # 总报价
        pay = request.POST['pay']
        #大写报价
        wordPay = request.POST['wordPay']
        # 服务期/工期
        time = request.POST['time']
        timemore = request.POST['timemore']
        # 法定代表人名称
        fddbrmc = request.POST['fddbrmc']
        # 被授权人姓名及身份证代码
        xmjsfzdm = request.POST['xmjsfzdm']
        # 被授权人电话
        bsqrdh = request.POST['bsqrdh']
        # 所属行业
        hy = request.POST['hy']
        # 编制日期
        bzrq = request.POST['bzrq']

        # 存储图片
        img_path = r"./img/username"
        if os.path.isdir(img_path):
            shutil.rmtree(img_path)

        os.mkdir(img_path)
        files = request.FILES.getlist('qtzhwj')
        for f in files:
            file = Yyzz_first(username=username,
                              img=f)
            file.save()
            print('上传成功')

        rep = redirect('/second/')

        rep.set_cookie('projectName', projectName)
        rep.set_cookie('projectNumber', projectNumber)
        rep.set_cookie('bossName', bossName)
        rep.set_cookie('pay', pay)
        rep.set_cookie('wordPay', wordPay)
        rep.set_cookie('time', time)
        rep.set_cookie('timemore', timemore)
        rep.set_cookie('fddbrmc', fddbrmc)
        rep.set_cookie('xmjsfzdm', xmjsfzdm)
        rep.set_cookie('bsqrdh', bsqrdh)
        rep.set_cookie('hy', hy)
        rep.set_cookie('bzrq', bzrq)
        return rep
    return render(request, 'first.html', ctx)

def sendPostFirst(request):
    ctx = {}
    return render(request, 'second.html', ctx)



