from django.shortcuts import render


from food_check import models

def calculate(foods):#接受一个QuerySet，计算各个指标每100g的平均含量，返回一个列表
    sum_kcal=0
    sum_carbo=0
    sum_protein=0
    sum_fat=0
    count_kcal=0
    count_carbo=0
    count_protein=0
    count_fat=0
    vlist=[]
    for food in foods:
        if(food.kcal):#判断是否为'None'
            sum_kcal+=food.kcal
            count_kcal+=1
        if(food.carbohydrate):
            sum_carbo+=food.carbohydrate
            count_carbo+=1
        if(food.protein):
            sum_protein+=food.protein
            count_protein+=1
        if(food.fat):
            sum_fat+=food.fat
            count_fat+=1

    if(count_kcal==0):#防止除数为0
        vlist.append(0)
    else:
        count=str(sum_kcal / count_kcal)[0:4]
        count_back=float(count)

        vlist.append(count_back)

    if(count_carbo==0):
        vlist.append(0)
    else:
        count=str(sum_carbo / count_carbo)[0:4]
        count_back=float(count)

        vlist.append(count_back)

    if(count_protein==0):
        vlist.append(0)
    else:
        count=str(sum_protein / count_protein)[0:4]
        count_back=float(count)

        vlist.append(count_back)
    if(count_fat==0):
        vlist.append(0)
    else:
        count=str(sum_fat / count_fat)[0:4]
        count_back=float(count)

        vlist.append(count_back)
    return vlist


def food01_check(request):
    food_list=models.Food01.objects.all()
    type_name=models.FoodTypeList.objects.filter(pk='01').get()
    vlist=calculate(food_list)
    val_list={'kcal_val':vlist[0],'carbo_val':vlist[1],#构建一个字典
             'protein_val':vlist[2],'fat_val':vlist[3]}
    context={'food_list':food_list,'type_name':type_name,'val_list':val_list}
    return render(request, 'food_check.html',context)

def food02_check(request):
    food_list=models.Food02.objects.all()
    type_name = models.FoodTypeList.objects.filter(pk='02').get()
    vlist = calculate(food_list)
    val_list = {'kcal_val': vlist[0], 'carbo_val': vlist[1],  # 构建一个字典
                'protein_val': vlist[2], 'fat_val': vlist[3]}
    context = {'food_list': food_list, 'type_name': type_name, 'val_list': val_list}
    return render(request, 'food_check.html',context)

def food03_check(request):
    food_list=models.Food03.objects.all()
    type_name = models.FoodTypeList.objects.filter(pk='03').get()
    vlist = calculate(food_list)
    val_list = {'kcal_val': vlist[0], 'carbo_val': vlist[1],  # 构建一个字典
                'protein_val': vlist[2], 'fat_val': vlist[3]}
    context = {'food_list': food_list, 'type_name': type_name, 'val_list': val_list}
    return render(request, 'food_check.html',context)

def food04_check(request):
    food_list=models.Food04.objects.all()
    type_name = models.FoodTypeList.objects.filter(pk='04').get()
    vlist = calculate(food_list)
    val_list = {'kcal_val': vlist[0], 'carbo_val': vlist[1],  # 构建一个字典
                'protein_val': vlist[2], 'fat_val': vlist[3]}
    context = {'food_list': food_list, 'type_name': type_name, 'val_list': val_list}
    return render(request, 'food_check.html',context)

def food05_check(request):
    food_list=models.Food05.objects.all()
    type_name = models.FoodTypeList.objects.filter(pk='05').get()
    vlist = calculate(food_list)
    val_list = {'kcal_val': vlist[0], 'carbo_val': vlist[1],  # 构建一个字典
                'protein_val': vlist[2], 'fat_val': vlist[3]}
    context = {'food_list': food_list, 'type_name': type_name, 'val_list': val_list}
    return render(request, 'food_check.html',context)

def food06_check(request):
    food_list=models.Food06.objects.all()
    type_name = models.FoodTypeList.objects.filter(pk='06').get()
    vlist = calculate(food_list)
    val_list = {'kcal_val': vlist[0], 'carbo_val': vlist[1],  # 构建一个字典
                'protein_val': vlist[2], 'fat_val': vlist[3]}
    context = {'food_list': food_list, 'type_name': type_name, 'val_list': val_list}
    return render(request, 'food_check.html',context)

def food07_check(request):
    food_list=models.Food07.objects.all()
    type_name = models.FoodTypeList.objects.filter(pk='07').get()
    vlist = calculate(food_list)
    val_list = {'kcal_val': vlist[0], 'carbo_val': vlist[1],  # 构建一个字典
                'protein_val': vlist[2], 'fat_val': vlist[3]}
    context = {'food_list': food_list, 'type_name': type_name, 'val_list': val_list}
    return render(request, 'food_check.html',context)

def food08_check(request):
    food_list=models.Food08.objects.all()
    type_name = models.FoodTypeList.objects.filter(pk='08').get()
    vlist = calculate(food_list)
    val_list = {'kcal_val': vlist[0], 'carbo_val': vlist[1],  # 构建一个字典
                'protein_val': vlist[2], 'fat_val': vlist[3]}
    context = {'food_list': food_list, 'type_name': type_name, 'val_list': val_list}
    return render(request, 'food_check.html',context)

def food09_check(request):
    food_list=models.Food09.objects.all()
    type_name = models.FoodTypeList.objects.filter(pk='09').get()
    vlist = calculate(food_list)
    val_list = {'kcal_val': vlist[0], 'carbo_val': vlist[1],  # 构建一个字典
                'protein_val': vlist[2], 'fat_val': vlist[3]}
    context = {'food_list': food_list, 'type_name': type_name, 'val_list': val_list}
    return render(request, 'food_check.html',context)

def food10_check(request):
    food_list=models.Food10.objects.all()
    type_name = models.FoodTypeList.objects.filter(pk='10').get()
    vlist = calculate(food_list)
    val_list = {'kcal_val': vlist[0], 'carbo_val': vlist[1],  # 构建一个字典
                'protein_val': vlist[2], 'fat_val': vlist[3]}
    context = {'food_list': food_list, 'type_name': type_name, 'val_list': val_list}
    return render(request, 'food_check.html',context)

def food11_check(request):
    food_list=models.Food11.objects.all()
    type_name = models.FoodTypeList.objects.filter(pk='11').get()
    vlist = calculate(food_list)
    val_list = {'kcal_val': vlist[0], 'carbo_val': vlist[1],  # 构建一个字典
                'protein_val': vlist[2], 'fat_val': vlist[3]}
    context = {'food_list': food_list, 'type_name': type_name, 'val_list': val_list}
    return render(request, 'food_check.html',context)

def food12_check(request):
    food_list=models.Food12.objects.all()
    type_name = models.FoodTypeList.objects.filter(pk='12').get()
    vlist = calculate(food_list)
    val_list = {'kcal_val': vlist[0], 'carbo_val': vlist[1],  # 构建一个字典
                'protein_val': vlist[2], 'fat_val': vlist[3]}
    context = {'food_list': food_list, 'type_name': type_name, 'val_list': val_list}
    return render(request, 'food_check.html',context)

def food13_check(request):
    food_list=models.Food13.objects.all()
    type_name = models.FoodTypeList.objects.filter(pk='13').get()
    vlist = calculate(food_list)
    val_list = {'kcal_val': vlist[0], 'carbo_val': vlist[1],  # 构建一个字典
                'protein_val': vlist[2], 'fat_val': vlist[3]}
    context = {'food_list': food_list, 'type_name': type_name, 'val_list': val_list}
    return render(request, 'food_check.html',context)

def food14_check(request):
    food_list=models.Food14.objects.all()
    type_name = models.FoodTypeList.objects.filter(pk='14').get()
    vlist = calculate(food_list)
    val_list = {'kcal_val': vlist[0], 'carbo_val': vlist[1],  # 构建一个字典
                'protein_val': vlist[2], 'fat_val': vlist[3]}
    context = {'food_list': food_list, 'type_name': type_name, 'val_list': val_list}
    return render(request, 'food_check.html',context)

def food15_check(request):
    food_list=models.Food15.objects.all()
    type_name = models.FoodTypeList.objects.filter(pk='15').get()
    vlist = calculate(food_list)
    val_list = {'kcal_val': vlist[0], 'carbo_val': vlist[1],  # 构建一个字典
                'protein_val': vlist[2], 'fat_val': vlist[3]}
    context = {'food_list': food_list, 'type_name': type_name, 'val_list': val_list}
    return render(request, 'food_check.html',context)

def food16_check(request):
    food_list=models.Food16.objects.all()
    type_name = models.FoodTypeList.objects.filter(pk='16').get()
    vlist = calculate(food_list)
    val_list = {'kcal_val': vlist[0], 'carbo_val': vlist[1],  # 构建一个字典
                'protein_val': vlist[2], 'fat_val': vlist[3]}
    context = {'food_list': food_list, 'type_name': type_name, 'val_list': val_list}
    return render(request, 'food_check.html',context)

def food17_check(request):
    food_list=models.Food17.objects.all()
    type_name = models.FoodTypeList.objects.filter(pk='17').get()
    vlist = calculate(food_list)
    val_list = {'kcal_val': vlist[0], 'carbo_val': vlist[1],  # 构建一个字典
                'protein_val': vlist[2], 'fat_val': vlist[3]}
    context = {'food_list': food_list, 'type_name': type_name, 'val_list': val_list}
    return render(request, 'food_check.html',context)

def food18_check(request):
    food_list=models.Food18.objects.all()
    type_name = models.FoodTypeList.objects.filter(pk='18').get()
    vlist = calculate(food_list)
    val_list = {'kcal_val': vlist[0], 'carbo_val': vlist[1],  # 构建一个字典
                'protein_val': vlist[2], 'fat_val': vlist[3]}
    context = {'food_list': food_list, 'type_name': type_name, 'val_list': val_list}
    return render(request, 'food_check.html',context)

def food19_check(request):
    food_list=models.Food19.objects.all()
    type_name = models.FoodTypeList.objects.filter(pk='19').get()
    vlist = calculate(food_list)
    val_list = {'kcal_val': vlist[0], 'carbo_val': vlist[1],  # 构建一个字典
                'protein_val': vlist[2], 'fat_val': vlist[3]}
    context = {'food_list': food_list, 'type_name': type_name, 'val_list': val_list}
    return render(request, 'food_check.html',context)

def food20_check(request):
    food_list=models.Food20.objects.all()
    type_name = models.FoodTypeList.objects.filter(pk='20').get()
    vlist = calculate(food_list)
    val_list = {'kcal_val': vlist[0], 'carbo_val': vlist[1],  # 构建一个字典
                'protein_val': vlist[2], 'fat_val': vlist[3]}
    context = {'food_list': food_list, 'type_name': type_name, 'val_list': val_list}
    return render(request, 'food_check.html',context)

def food21_check(request):
    food_list=models.Food21.objects.all()
    type_name = models.FoodTypeList.objects.filter(pk='21').get()
    vlist = calculate(food_list)
    val_list = {'kcal_val': vlist[0], 'carbo_val': vlist[1],  # 构建一个字典
                'protein_val': vlist[2], 'fat_val': vlist[3]}
    context = {'food_list': food_list, 'type_name': type_name, 'val_list': val_list}
    return render(request, 'food_check.html',context)
