from django.http import HttpResponse
from django.shortcuts import render
from .models import Book
# Create your views here.



def view_index(request):
    all_book = Book.objects.all()
    return render(request,"book_store/index.html",locals())

def set_cookies(request):

    response = HttpResponse("set cookie is ok")
    response.set_cookie("uname","gxn",500)

    return response


def set_session(request):
    request.session["uname"] = "wwc"
    return HttpResponse("set sesstion is ok")

def get_session(request):
    value = request.session["uname"]
    return HttpResponse(value)
