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

def page_not_found(request, exception):
    return redirect('/login/')
    # return render(request, 'login.html', status=404)

# def page_not_found_500(request, exception):
#     return render(request, 'login.html', status=500)