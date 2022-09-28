from django.shortcuts import render

# Create your views here.
def third(request):
    ctx = {}

    return render(request, 'third.html', ctx)