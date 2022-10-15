import time
import traceback

from django.http import StreamingHttpResponse
from django.shortcuts import render, redirect
from django.utils.encoding import escape_uri_path
from docx2pdf import convert

# import pythoncom


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
        # pythoncom.CoInitialize()
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
        # pythoncom.CoInitialize()
        zxqy_path = r"./tmp/{}_zxqy.docx".format(username)

        inputFile = zxqy_path
        outputFile = r"./tmp/output/{}_zxqy.pdf".format(username)
        file = open(outputFile, "w")
        file.close()

        convert(inputFile, outputFile)

        def down_chunk_file_manager(file_path, chuck_size=1024):
            with open(file_path, "rb") as file:
                while True:
                    chuck_stream = file.read(chuck_size)
                    if chuck_stream:
                        yield chuck_stream
                    else:
                        break

        response = StreamingHttpResponse(down_chunk_file_manager(outputFile))
        response['Content-Type'] = 'application/octet-stream'
        the_file_name = "中小企业声明函.pdf"
        # response["Content-Disposition"] = "attachment; filename*=UTF-8''{}".format(escape_uri_path(filename))
        response["Content-Disposition"] = "attachment; filename*=UTF-8''{}".format(escape_uri_path(the_file_name))

        return response
    except Exception as e:
        print(traceback.format_exc())
        return redirect('/third')
    return render(request, 'pdf.html', ctx)
