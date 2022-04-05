from django.http import HttpResponse
from django.shortcuts import render
from .models import User
# Create your views here.


def view_register(request):
    if request.method == "GET":
        return render(request,"user/register.html")
    elif request.method == "POST":
        username = request.POST["username"]
        p1 = request.POST["password_1"]
        p2 = request.POST["password_2"]

        #密码保持一致
        if p1 != p2:
            return HttpResponse("两次密码输入不一致")
        
        # 当前用户名是否可用

        old_users = User.objects.filter(user_name = username)
        if old_users:
            return HttpResponse("用户名已注册")
        User.objects.create(user_name=username,password = p1)
        return HttpResponse("注册成功")
