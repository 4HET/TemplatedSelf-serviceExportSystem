import time

from django.shortcuts import render, redirect

from Register import models
from Second.models import IMG, Bsqr, SF, Fbm, Yyzz, GZ


# Create your views here.
def register(request):
    # 定义一个错误提示为空
    error_name = ''
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # 供应商名称
        SupplierName = request.POST.get('SupplierName')
        # 联系电话
        phone = request.POST.get('phone')
        # 联系地址
        address = request.POST.get('address')
        # 电子邮箱
        email = request.POST.get('email')
        # 供应商开户行
        SupplierDepositBank = request.POST.get('SupplierDepositBank')
        # 供应商对公账号
        SupplierCorporateAccountNumber = request.POST.get('SupplierCorporateAccountNumber')
        # 企业从业人数
        NumberOfEmployees = request.POST.get('NumberOfEmployees')
        # 每年营业收入
        AnnualOperatingIncome = request.POST.get('AnnualOperatingIncome')
        # 资产总额
        TotalAssets = request.POST.get('TotalAssets')
        # 属于微型企业
        IsMicroEnterprise = request.POST.get('IsMicroEnterprise')
        user_list = models.User.objects.filter(username=username)
        if user_list:
            # 注册失败
            error_name = '%s用户名已经存在了' % username
            # 返回到注册页面，并且把错误信息报出来
            return render(request, 'register.html', {'error_name': error_name})
        else:
            # 数据保存在数据库中，并返回到登录页面
            user = models.User.objects.create(username=username,
                                              password=password,
                                              email=email,
                                              SupplierName=SupplierName,
                                              phone=phone,
                                              address=address,
                                              SupplierDepositBank=SupplierDepositBank,
                                              SupplierCorporateAccountNumber=SupplierCorporateAccountNumber,
                                              NumberOfEmployees=NumberOfEmployees,
                                              AnnualOperatingIncome=AnnualOperatingIncome,
                                              TotalAssets=TotalAssets,
                                              IsMicroEnterprise=IsMicroEnterprise
                                              )
            user.save()

            # 公章
            new_img = GZ(
                img=request.FILES.get('gz'),
                # name=name,
                name=request.FILES.get('gz').name,
                username=username,
            )
            new_img.save()

            img = GZ.objects.get(username=username)
            img.img = request.FILES.get('gz')
            img.name = request.FILES.get('gz').name
            img.img.name = username + '_gz.png'
            print(img.img.url)
            img.save()

            # 签名
            new_img = SF(
                img=request.FILES.get('sf'),
                name=request.FILES.get('sf').name,
                username=username
            )
            new_img.save()

            img = SF.objects.get(username=username)
            img.img = request.FILES.get('sf')
            img.name = request.FILES.get('sf').name
            img.img.name = username + '_sf.png'
            print(img.img.url)
            print("not exists!")
            img.save()
            # time.sleep(3)

            # 法定代表人身份证正面
            new_img = Bsqr(
                img=request.FILES.get('zm'),
                # name=name,
                name=request.FILES.get('zm').name,
                username=username
            )
            new_img.save()

            img = Bsqr.objects.get(username=username)
            img.img = request.FILES.get('zm')
            img.name = request.FILES.get('zm').name
            img.img.name = username + '_fzm.png'
            print(img.img.url)
            img.save()

            # 法定代表人身份证背面
            new_img = Fbm(
                img=request.FILES.get('bm'),
                # name=name,
                name=request.FILES.get('bm').name,
                username=username
            )
            new_img.save()

            img = Fbm.objects.get(username=username)
            img.img = request.FILES.get('bm')
            img.name = request.FILES.get('bm').name
            img.img.name = username + '_fbm.png'
            print(img.img.url)
            img.save()

            # 营业执照
            new_img = Yyzz(
                img=request.FILES.get('yyzz'),
                # name=name,
                name=request.FILES.get('yyzz').name,
                username=username
            )
            new_img.save()

            img = Yyzz.objects.get(username=username)
            img.img = request.FILES.get('yyzz')
            img.name = request.FILES.get('yyzz').name
            img.img.name = username + '_yyzz.png'
            print(img.img.url)
            img.save()

            return redirect('/login/')
    return render(request, 'register.html', {})
