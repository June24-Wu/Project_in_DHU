from django.shortcuts import render, redirect
from django import forms
from signup_login import models
from django.views.decorators import csrf
from django.db import connection
import datetime

from django.http import HttpResponse

from django.template import loader



def login(request):
    if request.method == "POST":
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        if username and password:  # 确保用户名和密码都不为空
            try:
                user = models.UserInfo.objects.get(username=username)
            except:
                message='用户不存在'
                return render(request, 'login.html',{'message':message})
            if user.password == password:
                request.session['user'] = user.username
                request.session.save()

                return redirect('/jump/')
            else:
                message='密码错误'
                return render(request, 'login.html',{'message':message})

    return render(request, 'login.html')


def register(request):
    if request.method == "POST":
        username = request.POST.get('username', None)
        password1 = request.POST.get('password1', None)
        password2 = request.POST.get('password2', None)
        if password1 != password2:  # 判断两次密码是否相同
            message = "两次输入的密码不同！"
            return render(request, 'register.html',{'message':message} )
        else:

            same_name_user = models.UserInfo.objects.filter(username=username)
            if same_name_user:  # 用户名唯一
                message = '用户已经存在，请重新选择用户名！'
                return render(request, 'register.html', {'message':message})

            # 当一切都OK的情况下，创建新用户
            new_user = models.UserInfo.objects.create()
            new_user.username = username
            new_user.password = password1
            new_user.save()
            return redirect('/login/')  # 自动跳转到登录页面
    return render(request, 'register.html')


def index(request):
    if request.method == "POST":
        return render(request, 'login.html')  # 自动跳转到登录页面
    return render(request, 'index.html')


def logout(request):
    request.sessions.clear()
    return render(request, 'index.html')


def turntoreg(request):
    return render(request, 'login.html')


def update(request):
    if request.method == "POST":
        return render(request, 'checkout.html')
    return render(request, "jump.html")


def weight(request):#体重更新
    if request.method == "POST":
        weight = request.POST.get('weight')
        username = request.session['user']
        user = models.UserInfo.objects.filter(username=username)
        if user:
            new_user = models.UserWeight.objects.create()
            new_user.username = username
            new_user.weight = weight
            new_user.save()
 
    return render(request, 'checkout.html')


def height(request):#身高更新
    if request.method == "POST":
        height = request.POST.get('height')
        username = request.session['user']
        user = models.UserHeight.objects.filter(username=username)
        if user:
            user_exsist = models.UserHeight.objects.get(username=username)
            if user_exsist:
                user_exsist.height=height
                user_exsist.save()
            else:
                new_user = models.UserHeight.objects.create()
                new_user.username = username
                new_user.height = height
                new_user.save()

    return render(request,  'checkout.html')




def waist(request):#腰围更新
    if request.method == "POST":
        waist = request.POST.get('waist')
        username = request.session['user']
        user = models.UserInfo.objects.filter(username=username)
        if user:
            new_user = models.UserWaist.objects.create()
            new_user.username = username
            new_user.waist = waist
            new_user.save()

    
    return render(request,  'checkout.html')


def food_check(request):#跳转页面设置这个你不用管
        return render(request,'food_check.html')

def blood_sugar(request):#血糖更新
    if request.method == "POST":
        blood_sugar = request.POST.get('blood_sugar')
        username = request.session['user']
        user = models.UserInfo.objects.filter(username=username)
        if user:
            new_user = models.Userbloodsugar.objects.create()
            new_user.username = username
            new_user.bloodsugar = blood_sugar
            new_user.save()

    
    return render(request,  'checkout.html')


def blood_pressure(request):#血脂更新
    if request.method == "POST":
        blood_pressure = request.POST.get('blood_pressure')
        username = request.session['user']
        user_exsist = models.UserInfo.objects.filter(username=username)
        if user_exsist:
            
            new_user = models.Userbloodpressure.objects.create()
            new_user.username = username
            new_user.bloodpressure = blood_pressure
            new_user.save()

    return render(request,  'checkout.html')



def weight_picture(request): #传echarts画图
    username = request.session['user']
    weight_list_all = models.UserWeight.objects.filter(username=username)
    weight_list = []
    weight_time_list = []
    for weight in weight_list_all:
        time_info = datetime.datetime.strftime(weight.time, "%Y-%m-%d")
        weight_list.append(weight.weight)
        weight_time_list.append(time_info.replace("'", ""))

    waist_list_all = models.UserWaist.objects.filter(username=username)
    waist_list = []
    waist_time_list = []
    for waist in waist_list_all:
        time_info = datetime.datetime.strftime(waist.time, "%Y-%m-%d")
        waist_list.append(waist.waist)
        waist_time_list.append(time_info.replace("'", ""))
    
    height=models.UserHeight.objects.get(username=username)
    height=height.height
    bmi=[]
    for weight in weight_list_all:
        weight_user=weight.weight
        bmi_user=weight_user/((height*0.01))/((height*0.01))
        bmi.append(bmi_user)


    bloodsugar_list_all = models.Userbloodsugar.objects.filter(
        username=username)
    bloodsugar_list = []
    bloodsugar_time_list = []
    for bloodsugar in bloodsugar_list_all:
        time_info = datetime.datetime.strftime(bloodsugar.time, "%Y-%m-%d")
        bloodsugar_list.append(bloodsugar.bloodsugar)
        bloodsugar_time_list.append(time_info.replace("'", ""))

    bloodpressure_list_all = models.Userbloodpressure.objects.filter(
        username=username)
    bloodpressure_list = []
    bloodpressure_time_list = []
    for bloodpressure in bloodpressure_list_all:
        time_info = datetime.datetime.strftime(bloodpressure.time, "%Y-%m-%d")
        bloodpressure_list.append(bloodpressure.bloodpressure)
        bloodpressure_time_list.append(time_info.replace("'", ""))

    height=models.UserHeight.objects.filter(username=username)
    

    return render(request, 'jump.html', {'weight_list': weight_list, 'weight_time_list': weight_time_list,
                                         'waist_list': waist_list, 'waist_time_list': waist_time_list,
                                         'bmi':bmi, 'weight_time_list': weight_time_list,
                                         'bloodsugar_list':bloodsugar_list,'bloodsugar_time_list':bloodsugar_time_list,
                                         'bloodpressure_list':bloodpressure_list,'bloodpressure_time_list':bloodpressure_time_list
                                         })
