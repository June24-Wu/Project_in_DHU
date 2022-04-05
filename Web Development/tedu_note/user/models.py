from django.db import models

# Create your models here.

class User(models.Model):
    user_name = models.CharField("用户名",max_length=50,unique=True)
    password = models.CharField("密码",max_length=32)
    create_time = models.DateTimeField("创建时间",auto_now_add=True)
    update_time = models.DateTimeField("更新时间",auto_now=True)
    def __str__(self) -> str:
        return "用户ID： %s" % self.user_name
    class Meta:
        db_table = "Users"