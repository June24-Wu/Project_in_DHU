from django.shortcuts import render
from .models import Book
# Create your views here.



def view_index(request):
    all_book = Book.objects.all()
    return render(request,"book_store/index.html",locals())
