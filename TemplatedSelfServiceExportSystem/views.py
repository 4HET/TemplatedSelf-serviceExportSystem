from django.shortcuts import render, redirect

from Register import models


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user_obj = models.User.objects.filter(username=username, password=password).first()
        except:
            user_obj = False

        if not user_obj:
            return redirect("/login/")
        else:
            rep = redirect("/first/")
            rep.set_cookie("is_login", True)
            rep.set_cookie("username", username)
            rep.set_cookie("password", password)
            return rep
    return render(request, 'login.html', {})

