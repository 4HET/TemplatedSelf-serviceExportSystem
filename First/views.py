from django.shortcuts import render, redirect


# Create your views here.
def first(request):
    ctx = {}
    status = request.COOKIES.get('is_login')

    if not status:
        return redirect('/login/')
    if request.method == 'POST':
        # 项目名称
        projectName = request.POST['projectName']
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

        rep = redirect('/second/')
        rep.set_cookie('projectName', projectName)
        rep.set_cookie('projectNumber', projectNumber)
        rep.set_cookie('bossName', bossName)
        rep.set_cookie('pay', pay)
        rep.set_cookie('wordPay', wordPay)
        rep.set_cookie('time', time)
        return rep
    return render(request, 'first.html', ctx)

def sendPostFirst(request):
    ctx = {}
    return render(request, 'second.html', ctx)