from django.contrib import admin
from .models import Book , Author
# Register your models here.



class BookManager(admin.ModelAdmin):
    list_display = ["id","title","pub","price","market_price"]
    list_display_links = ["title"]
    list_filter = ["pub","price"]

    # 添加搜索框
    search_filed = ["title"]

class AuthorManager(admin.ModelAdmin):
    list_display = ["name","age","email"]


    
admin.site.register(Book,BookManager)
admin.site.register(Author,AuthorManager)