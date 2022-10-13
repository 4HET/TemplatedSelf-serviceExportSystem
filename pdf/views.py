from django.shortcuts import render, redirect


# Create your views here.
def pdf(request):
    ctx = {}
    status = request.COOKIES.get('is_login')
    if not status:
        return redirect('/login/')
    return render(request, 'pdf.html', ctx)