from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
# from .models import User
import hashlib
from django.contrib.auth import authenticate, login, logout , models
from django.contrib.auth.models import User
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

        old_users = User.objects.filter(username = username)
        if old_users:
            return HttpResponse("用户名已注册")

        try: # 处理并发
            user = User.objects.create_user(username=username,password = p1)
            user.save()
        except Exception as e:
            print("-- create user error %s" % (e))
            return HttpResponse("用户名已注册")

        # 免登陆一天
        request.session["username"] = username
        request.session["uid"] = user.id
        
        return HttpResponseRedirect("/")

def view_login(request):
    if request.method == "GET":
        # 检查登录状态
        if request.session.get("username") and request.session.get("uid"):
            return HttpResponseRedirect("/")
        c_username = request.COOKIES.get("username")
        c_uid = request.COOKIES.get("uid")
        if c_username and c_uid:
            request.session["username"] = c_username
            request.session["uid"] = c_uid
            return HttpResponseRedirect("/")
        # 获取login页面
        return render(request,"user/login.html")
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            # 免登陆一天
            request.session["user_name"] = username
            request.session["uid"] = user.id
            response = HttpResponseRedirect("/")

            # 判断用户是否点选了“记住用户名
            if "remember" in request.POST:
                response.set_cookie("user_name",username,3600*24*30)
                response.set_cookie("uid",user.id,3600*24*30)
            return response
        else: return HttpResponse("用户名或密码错误")
def view_logout(request):
    if "uid" in request.COOKIES:
        del request.COOKIES["uid"] 
    if "user_name" in request.COOKIES:
        del request.COOKIES["user_name"]
    logout(request)
    html = HttpResponseRedirect("/")
    html.delete_cookie("user_name")
    html.delete_cookie("uid")
    return html

