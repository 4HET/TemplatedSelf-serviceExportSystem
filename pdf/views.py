import time
import traceback

from django.shortcuts import render, redirect
from docx2pdf import convert

import pythoncom

# Create your views here.
def pdf(request):
    ctx = {}
    username = request.COOKIES.get("username")
    status = request.COOKIES.get('is_login')
    if not status:
        return redirect('/login/')
    return render(request, 'pdf.html', ctx)

def xywjpdf(request):
    ctx = {}
    username = request.COOKIES.get("username")
    status = request.COOKIES.get('is_login')
    if not status:
        return redirect('/login/')
    try:
        pythoncom.CoInitialize()
        xywj_path = r"./tmp/{}_final.docx".format(username)
        # xywj_path = r"./tmp/test.docx"

        inputFile = xywj_path
        outputFile = r"./tmp/output/{}_xywj.pdf".format(username)
        file = open(outputFile, "w")
        file.close()

        convert(inputFile, outputFile)

        print("hhh")
    except Exception as e:
        print(traceback.format_exc())
        return redirect('/third')
    return render(request, 'pdf.html', ctx)

def zxqypdf(request):
    ctx = {}
    username = request.COOKIES.get("username")
    status = request.COOKIES.get('is_login')
    if not status:
        return redirect('/login/')
    try:
        pythoncom.CoInitialize()
        zxqy_path = r".\tmp\{}_zxqy.docx".format(username)

        inputFile = zxqy_path
        outputFile = r".\tmp\output\{}_zxqy.pdf".format(username)
        file = open(outputFile, "w")
        file.close()

        convert(inputFile, outputFile)
    except Exception as e:
        print(traceback.format_exc())
        return redirect('/third')
    return render(request, 'pdf.html', ctx)