from django.shortcuts import render

# Create your views here.
def second(request):
    context = {}
    context['hello'] = 'Hello World!'
    return render(request, 'second.html', context)