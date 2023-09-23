from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User

# Create your views here.


def HomePage(request):
    return render(request,"home.html")

def SignupPage(request):
    if request.method=="POST":
        uname = request.POST.get("username")
        email = request.POST.get("email")
        pass1 = request.POST.get("password1")
        pass2 = request.POST.get("password2")

        if pass1!=pass2:
            return HttpResponse("Password Mismatched")
        else:
            my_user = User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect("login")
        
        # print(uname,email,pass1)


    return render(request,"signup.html")

def LoginPage(request):
    if request.method=="POST":
        username = request.POST.get("username")
        pass1 = request.POST.get("pass")

        print(username,pass1)
    return render(request,"login.html")