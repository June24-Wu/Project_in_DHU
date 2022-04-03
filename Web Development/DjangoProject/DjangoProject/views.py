import imp
from unittest import result
from django.http import HttpResponse , HttpResponseRedirect
from django.template import loader
from django.shortcuts import render


Post_Form = """
<form method='post' action='/test_get_post'>
    用户名: <input type='test' name='uname'>
    <input type='submit' value='提交'>
</form>
"""
def page_2003_view(request):
    html = "<h1>这是第一个页面<h1>"
    return HttpResponse(html)

def main_page_view(request):
    html = "<h1>这是我的首页<h1>"
    return HttpResponse(html)

def page_1_view(request):
    html = "<h1>这是我的第一个页面<h1>"
    return HttpResponse(html)

def page_2_view(request):
    html = "<h1>这是我的第二个页面<h1>"
    return HttpResponse(html)  

def pagen_view(request,page_name):
    html = "<h1>这是编号为%s的页面<h1>" % (page_name)
    return HttpResponse(html)  

def cal_view(request,n,func = "add",m = 1):
    if func not in ["add","sub","mul"]:
        return HttpResponse("Your func is wrong")
    if func == "add":
        html = "<h1>%s + %s = %s" % (n,m,n+m)
    if func == "sub":
        html = "<h1>%s - %s = %s" % (n,m,n-m)
    if func == "mul":
        html = "<h1>%s * %s = %s" % (n,m,n*m)
    return HttpResponse(html)  

def redirect(request):
    return HttpResponseRedirect("/page/1")

def test_get_post(request):

    if request.method == "GET":
        return HttpResponse(Post_Form)
    if request.method == "POST":
        return HttpResponse("user name is " + request.POST.get("uname"))


    return HttpResponse("-- Get Post Ok --")

def calculator2(request):
    if request.method == "GET":
        n = int(request.GET.get("a"))
        m = int(request.GET.get("b"))
        func = request.GET.get("op")
        if func == "+":
            html = "<h1>%s + %s = %s" % (n,m,n+m)
        if func == "-":
            html = "<h1>%s - %s = %s" % (n,m,n-m)
        if func == "*":
            html = "<h1>%s * %s = %s" % (n,m,n*m)
        return HttpResponse(html)
    return HttpResponse("No Val")

def test_html(request):

    # 方案1
    # html = loader.get_template("test_html.html").render()
    # return HttpResponse(html)

    # 方案2
    # return render(request,"test_html.html")

    dic = {"username":"June","age":18}
    return render(request,"test_html.html",dic)

def test_if_for(request):
    dic = {}
    dic["y"] = {"June","6","24"}
    return render(request,"test_if_for.html",dic)

def calculator3(request):
    if request.method == "GET":
        return render(request,"calculator.html")
    if request.method == "POST":
        m = int(request.POST["x"])
        n = int(request.POST["y"])
        op = request.POST["op"]
        
        result = 0
        if op == "add":
            result =  m+n
        if op == "sub":
            result =  m-n
        if op == "mul":
            result =  m*n
        if op == "div":
            result =  m / n

        return render(request,"calculator.html",locals())



# 继承
def base_view(request):
    return render(request,"base.html")
def music_view(request):
    return render(request,"music.html")
def sport_view(request):
    return render(request,"sport.html")


# 静态文件
def test_static(request):
    return render(request,"test_static.html")



    
