from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

# Create your views here.

def user_login(request):
    if request.user.is_authenticated:
        return redirect("index")

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("index")
        else:
            return render(request, "account/login.html", { "error":"Username or Password is incorrect"})
    else:
        return render(request, "account/login.html")

def user_register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        re_password = request.POST["re_password"]

        if password == re_password:
            if User.objects.filter(username = username).exists():
                return render(request, "account/register.html", { "error":"Username is used, Please enter another username value", "username": username, "email": email})
            else:
              if User.objects.filter(email = email).exists():
                  return render(request, "account/register.html", { "error":"Email is used, Please enter another email value", "username": username, "email": email})
              else:
                  user = User.objects.create_user(username = username, email = email, password = password)
                  user.save()
                  return redirect("user_login")
        else:
            return render(request, "account/register.html", { "error":"Passwords do not match", "username": username, "email": email})
    else:
        return render(request, "account/register.html")

def user_logout(request):
    logout(request)
    return redirect("index")
