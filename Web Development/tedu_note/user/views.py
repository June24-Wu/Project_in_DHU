from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import User
import hashlib
# Create your views here.


def view_register(request):
    if request.method == "GET":
        return render(request,"user/register.html")
    elif request.method == "POST":
        username = request.POST["username"]
        p1 = request.POST["password_1"]
        p2 = request.POST["password_2"]
        hash_code = hashlib.sha256()
        hash_code.update(p1.encode("utf-8"))
        hash_code = hash_code.hexdigest()
        #密码保持一致
        if p1 != p2:
            return HttpResponse("两次密码输入不一致")
        
        # 当前用户名是否可用

        old_users = User.objects.filter(user_name = username)
        if old_users:
            return HttpResponse("用户名已注册")

        try: # 处理并发
            user = User.objects.create(user_name=username,password = hash_code)
        except Exception as e:
            print("-- create user error %s" % (e))
            return HttpResponse("用户名已注册")

        # 免登陆一天
        request.session["user_name"] = username
        request.session["uid"] = user.id
        
        return HttpResponseRedirect("/")

def view_login(request):
    if request.method == "GET":
        # 检查登录状态
        if request.session.get("user_name") and request.session.get("uid"):
            return HttpResponseRedirect("/")
        c_username = request.COOKIES.get("user_name")
        c_uid = request.COOKIES.get("uid")
        if c_username and c_uid:
            request.session["user_name"] = c_username
            request.session["uid"] = c_uid
            return HttpResponseRedirect("/")
        # 获取login页面
        return render(request,"user/login.html")
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        try:
            user = User.objects.get(user_name=username)
        except Exception as e:
            print(" -- login user error : %s" % e)
            return HttpResponse("用户名或密码不正确")
        
        hash_code = hashlib.sha256()
        hash_code.update(password.encode("utf-8"))
        hash_code = hash_code.hexdigest()
        if hash_code != user.password:
            return HttpResponse("用户名或密码不正确")
        # 免登陆一天
        request.session["user_name"] = username
        request.session["uid"] = user.id


        response = HttpResponseRedirect("/")

        # 判断用户是否点选了“记住用户名
        if "remember" in request.POST:
            response.set_cookie("user_name",username,3600*24*30)
            response.set_cookie("uid",user.id,3600*24*30)
        return response

