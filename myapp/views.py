from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from .form import ImageForm
from .models import Image

# Create your views here.


def index(request):
    if request.method == "POST":
        form=ImageForm(data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            obj=form.instance
            return render(request,"index.html",{"obj":obj})
    else:
        form=ImageForm()
        img=Image.objects.all()
    return render(request,"index.html",{"img":img,"form":form})
    # return render(request,"home.html")

def SignupPage(request):
    if request.method=="POST":
        uname = request.POST.get("username")
        email = request.POST.get("email")
        pass1 = request.POST.get("password1")
        pass2 = request.POST.get("password2")

        if pass1!=pass2:
            return HttpResponse("Password Mismatched!!!")
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

        user = authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect("home")
        else:
            return HttpResponse("Username or Password is incorrect!!!")

        print(username,pass1)
    return render(request,"login.html")