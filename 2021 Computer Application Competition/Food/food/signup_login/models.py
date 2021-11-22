from django.db import models
#建立数据表
class UserInfo(models.Model):
    username=models.CharField(max_length=30)
    password=models.CharField(max_length=30)

class UserWeight(models.Model):
    username = models.CharField(max_length=30)
    weight = models.IntegerField(blank=True,null=True)
    time = models.DateField(auto_now_add=True)


class UserHeight(models.Model):
    username = models.CharField(max_length=30)
    height = models.IntegerField(blank=True,null=True)


class UserWaist(models.Model):
    username = models.CharField(max_length=30)
    waist = models.IntegerField(blank=True,null=True)
    time = models.DateField(auto_now_add=True)


class Userbloodsugar(models.Model):
    username = models.CharField(max_length=30)
    bloodsugar = models.IntegerField(blank=True,null=True)
    time = models.DateField(auto_now_add=True)


class Userbloodpressure(models.Model):
    username = models.CharField(max_length=30)
    bloodpressure = models.IntegerField(blank=True,null=True)
    time = models.DateField(auto_now_add=True)
