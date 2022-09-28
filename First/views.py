from django.shortcuts import render

# Create your views here.
def first(request):
    ctx = {}

    # ctx['projectName'] = request.POST["projectName"]
    # ctx['projectNumber'] = request.POST["projectNumber"]
    # ctx['bossName'] = request.POST["bossName"]
    # ctx['pay'] = request.POST["pay"]
    # ctx['wordPay'] = request.POST["wordPay"]
    # ctx['time'] = request.POST["time"]
    # ctx['submit'] = request.POST["submit"]
    return render(request, 'first.html', ctx)

def sendPostFirst(request):
    ctx = {}
    return render(request, 'second.html', ctx)