from pyexpat import model
from django.db import models

# Create your models here.


class Book(models.Model):
    title = models.CharField("书名",max_length=50,default="",unique=True)
    pub = models.CharField("出版社",max_length=100,null=False,default="")
    price = models.DecimalField("价格",max_digits=7,decimal_places=2)
    market_price = models.DecimalField("图书零售价",max_digits=7,decimal_places=2,default=0.0)
    info = models.CharField("信息",max_length=100,default="")
    class Meta:
        db_table = "book"
    def __str__(self) -> str:
        return self.title
class Author(models.Model):
    name = models.CharField("作者",max_length=11,default="",null=False)
    age = models.IntegerField("年龄",default=1)
    email = models.EmailField("邮箱",null=True)
    class Meta:
        db_table = "author"