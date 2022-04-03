from django.http import HttpRequest , HttpResponse
from django.shortcuts import render

# Create your views here.


def main_page_view(request):
    html = "<h1>这是我的音乐首页<h1>"
    return HttpResponse(html)