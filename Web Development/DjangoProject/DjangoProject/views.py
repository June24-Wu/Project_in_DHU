from django.http import HttpResponse , HttpResponseRedirect


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