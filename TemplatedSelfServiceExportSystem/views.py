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

print(r"""                     _           _   _             _  _   _    _ ______ _______ 
                    | |         | | | |           | || | | |  | |  ____|__   __|
  ___ _ __ ___  __ _| |_ ___  __| | | |__  _   _  | || |_| |__| | |__     | |   
 / __| '__/ _ \/ _` | __/ _ \/ _` | | '_ \| | | | |__   _|  __  |  __|    | |   
| (__| | |  __/ (_| | ||  __/ (_| | | |_) | |_| |    | | | |  | | |____   | |   
 \___|_|  \___|\__,_|\__\___|\__,_| |_.__/ \__, |    |_| |_|  |_|______|  |_|   
                                            __/ |                               
                                           |___/                            
""")