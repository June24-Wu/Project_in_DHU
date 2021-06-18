from django.db import models
class Food01(models.Model): #01代表食物编码的前两位，对应食物类别
    foodid = models.CharField(primary_key=True, max_length=26)
    foodname = models.CharField(max_length=128, blank=True, null=True)
    kcal = models.BigIntegerField(blank=True, null=True)
    carbohydrate = models.DecimalField(max_digits=38, decimal_places=1, blank=True, null=True)
    protein = models.DecimalField(max_digits=38, decimal_places=1, blank=True, null=True)
    fat = models.DecimalField(max_digits=38, decimal_places=1, blank=True, null=True)

    class Meta:
        managed = True #true意味着后面允许对表进行modification之类操作
        db_table = 'food01'


class Food02(models.Model):
    foodid = models.CharField(primary_key=True, max_length=26)
    foodname = models.CharField(max_length=128, blank=True, null=True)
    kcal = models.BigIntegerField(blank=True, null=True)
    carbohydrate = models.DecimalField(max_digits=38, decimal_places=1, blank=True, null=True)
    protein = models.DecimalField(max_digits=38, decimal_places=1, blank=True, null=True)
    fat = models.DecimalField(max_digits=38, decimal_places=1, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'food02'


class Food03(models.Model):
    foodid = models.CharField(primary_key=True, max_length=26)
    foodname = models.CharField(max_length=128, blank=True, null=True)
    kcal = models.BigIntegerField(blank=True, null=True)
    carbohydrate = models.DecimalField(max_digits=38, decimal_places=1, blank=True, null=True)
    protein = models.DecimalField(max_digits=38, decimal_places=1, blank=True, null=True)
    fat = models.DecimalField(max_digits=38, decimal_places=1, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'food03'


class Food04(models.Model):
    foodid = models.CharField(primary_key=True, max_length=26)
    foodname = models.CharField(max_length=128, blank=True, null=True)
    kcal = models.BigIntegerField(blank=True, null=True)
    carbohydrate = models.DecimalField(max_digits=38, decimal_places=1, blank=True, null=True)
    protein = models.DecimalField(max_digits=38, decimal_places=1, blank=True, null=True)
    fat = models.DecimalField(max_digits=38, decimal_places=1, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'food04'


class Food05(models.Model):
    foodid = models.CharField(primary_key=True, max_length=26)
    foodname = models.CharField(max_length=128, blank=True, null=True)
    kcal = models.BigIntegerField(blank=True, null=True)
    carbohydrate = models.DecimalField(max_digits=38, decimal_places=1, blank=True, null=True)
    protein = models.DecimalField(max_digits=38, decimal_places=1, blank=True, null=True)
    fat = models.DecimalField(max_digits=38, decimal_places=1, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'food05'


class Food06(models.Model):
    foodid = models.CharField(primary_key=True, max_length=26)
    foodname = models.CharField(max_length=128, blank=True, null=True)
    kcal = models.BigIntegerField(blank=True, null=True)
    carbohydrate = models.DecimalField(max_digits=38, decimal_places=1, blank=True, null=True)
    protein = models.DecimalField(max_digits=38, decimal_places=1, blank=True, null=True)
    fat = models.DecimalField(max_digits=38, decimal_places=1, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'food06'


class Food07(models.Model):
    foodid = models.CharField(primary_key=True, max_length=26)
    foodname = models.CharField(max_length=128, blank=True, null=True)
    kcal = models.BigIntegerField(blank=True, null=True)
    carbohydrate = models.DecimalField(max_digits=38, decimal_places=1, blank=True, null=True)
    protein = models.DecimalField(max_digits=38, decimal_places=1, blank=True, null=True)
    fat = models.DecimalField(max_digits=38, decimal_places=1, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'food07'


class Food08(models.Model):
    foodid = models.CharField(primary_key=True, max_length=26)
    foodname = models.CharField(max_length=128, blank=True, null=True)
    kcal = models.BigIntegerField(blank=True, null=True)
    carbohydrate = models.DecimalField(max_digits=38, decimal_places=1, blank=True, null=True)
    protein = models.DecimalField(max_digits=38, decimal_places=1, blank=True, null=True)
    fat = models.DecimalField(max_digits=38, decimal_places=1, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'food08'


class Food09(models.Model):
    foodid = models.CharField(primary_key=True, max_length=26)
    foodname = models.CharField(max_length=128, blank=True, null=True)
    kcal = models.BigIntegerField(blank=True, null=True)
    carbohydrate = models.DecimalField(max_digits=38, decimal_places=1, blank=True, null=True)
    protein = models.DecimalField(max_digits=38, decimal_places=1, blank=True, null=True)
    fat = models.DecimalField(max_digits=38, decimal_places=1, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'food09'


class Food10(models.Model):
    foodid = models.CharField(primary_key=True, max_length=26)
    foodname = models.CharField(max_length=128, blank=True, null=True)
    kcal = models.BigIntegerField(blank=True, null=True)
    carbohydrate = models.DecimalField(max_digits=38, decimal_places=1, blank=True, null=True)
    protein = models.DecimalField(max_digits=38, decimal_places=1, blank=True, null=True)
    fat = models.DecimalField(max_digits=38, decimal_places=1, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'food10'


class Food11(models.Model):
    foodid = models.CharField(primary_key=True, max_length=26)
    foodname = models.CharField(max_length=128, blank=True, null=True)
    kcal = models.BigIntegerField(blank=True, null=True)
    carbohydrate = models.DecimalField(max_digits=38, decimal_places=1, blank=True, null=True)
    protein = models.DecimalField(max_digits=38, decimal_places=1, blank=True, null=True)
    fat = models.DecimalField(max_digits=38, decimal_places=1, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'food11'


class Food12(models.Model):
    foodid = models.CharField(primary_key=True, max_length=26)
    foodname = models.CharField(max_length=128, blank=True, null=True)
    kcal = models.BigIntegerField(blank=True, null=True)
    carbohydrate = models.DecimalField(max_digits=38, decimal_places=1, blank=True, null=True)
    protein = models.DecimalField(max_digits=38, decimal_places=1, blank=True, null=True)
    fat = models.DecimalField(max_digits=38, decimal_places=1, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'food12'


class Food13(models.Model):
    foodid = models.CharField(primary_key=True, max_length=26)
    foodname = models.CharField(max_length=128, blank=True, null=True)
    kcal = models.BigIntegerField(blank=True, null=True)
    carbohydrate = models.DecimalField(max_digits=38, decimal_places=1, blank=True, null=True)
    protein = models.DecimalField(max_digits=38, decimal_places=1, blank=True, null=True)
    fat = models.DecimalField(max_digits=38, decimal_places=1, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'food13'


class Food14(models.Model):
    foodid = models.CharField(primary_key=True, max_length=26)
    foodname = models.CharField(max_length=128, blank=True, null=True)
    kcal = models.BigIntegerField(blank=True, null=True)
    carbohydrate = models.DecimalField(max_digits=38, decimal_places=1, blank=True, null=True)
    protein = models.DecimalField(max_digits=38, decimal_places=1, blank=True, null=True)
    fat = models.DecimalField(max_digits=38, decimal_places=1, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'food14'


class Food15(models.Model):
    foodid = models.CharField(primary_key=True, max_length=26)
    foodname = models.CharField(max_length=128, blank=True, null=True)
    kcal = models.BigIntegerField(blank=True, null=True)
    carbohydrate = models.DecimalField(max_digits=38, decimal_places=1, blank=True, null=True)
    protein = models.DecimalField(max_digits=38, decimal_places=1, blank=True, null=True)
    fat = models.DecimalField(max_digits=38, decimal_places=1, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'food15'


class Food16(models.Model):
    foodid = models.CharField(primary_key=True, max_length=26)
    foodname = models.CharField(max_length=128, blank=True, null=True)
    kcal = models.BigIntegerField(blank=True, null=True)
    carbohydrate = models.DecimalField(max_digits=38, decimal_places=1, blank=True, null=True)
    protein = models.DecimalField(max_digits=38, decimal_places=1, blank=True, null=True)
    fat = models.DecimalField(max_digits=38, decimal_places=1, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'food16'


class Food17(models.Model):
    foodid = models.CharField(primary_key=True, max_length=26)
    foodname = models.CharField(max_length=128, blank=True, null=True)
    kcal = models.BigIntegerField(blank=True, null=True)
    carbohydrate = models.DecimalField(max_digits=38, decimal_places=1, blank=True, null=True)
    protein = models.DecimalField(max_digits=38, decimal_places=1, blank=True, null=True)
    fat = models.DecimalField(max_digits=38, decimal_places=1, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'food17'


class Food18(models.Model):
    foodid = models.CharField(primary_key=True, max_length=26)
    foodname = models.CharField(max_length=128, blank=True, null=True)
    kcal = models.BigIntegerField(blank=True, null=True)
    carbohydrate = models.DecimalField(max_digits=38, decimal_places=1, blank=True, null=True)
    protein = models.DecimalField(max_digits=38, decimal_places=1, blank=True, null=True)
    fat = models.DecimalField(max_digits=38, decimal_places=1, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'food18'


class Food19(models.Model):
    foodid = models.CharField(primary_key=True, max_length=26)
    foodname = models.CharField(max_length=128, blank=True, null=True)
    kcal = models.BigIntegerField(blank=True, null=True)
    carbohydrate = models.DecimalField(max_digits=38, decimal_places=1, blank=True, null=True)
    protein = models.DecimalField(max_digits=38, decimal_places=1, blank=True, null=True)
    fat = models.DecimalField(max_digits=38, decimal_places=1, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'food19'


class Food20(models.Model):
    foodid = models.CharField(primary_key=True, max_length=26)
    foodname = models.CharField(max_length=128, blank=True, null=True)
    kcal = models.BigIntegerField(blank=True, null=True)
    carbohydrate = models.DecimalField(max_digits=38, decimal_places=1, blank=True, null=True)
    protein = models.DecimalField(max_digits=38, decimal_places=1, blank=True, null=True)
    fat = models.DecimalField(max_digits=38, decimal_places=1, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'food20'


class Food21(models.Model):
    foodid = models.CharField(primary_key=True, max_length=26)
    foodname = models.CharField(max_length=128, blank=True, null=True)
    kcal = models.BigIntegerField(blank=True, null=True)
    carbohydrate = models.DecimalField(max_digits=38, decimal_places=1, blank=True, null=True)
    protein = models.DecimalField(max_digits=38, decimal_places=1, blank=True, null=True)
    fat = models.DecimalField(max_digits=38, decimal_places=1, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'food21'

class FoodTypeList(models.Model):#一个表，对应着21个类别的名字
    typeid = models.CharField(primary_key=True, max_length=26)
    typename = models.CharField(max_length=128)

    class Meta:
        managed = True
        db_table = 'food_type_list'

# Create your models here.
