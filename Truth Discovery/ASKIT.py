#coding:utf-8
import math
import pandas as pd
import xlrd
from math import *
import random
from time import *

begin_time = time()


# 打开文件groundtruth表
workBooktruth = xlrd.open_workbook('F:\Desktop\esttruth.xls');

## 按索引号获取sheet内容
sheet1_truthcontent1 = workBooktruth.sheet_by_index(0); # sheet索引从0开始

# 获取整行和整列的值（数组）
tru1 = sheet1_truthcontent1.col_values(0); # 获取第一列内容
tru2 = sheet1_truthcontent1.col_values(1); # 获取第二列内容
for i in range(10):
    tru2[i] = tru2[i]/2
print tru2


# 打开文件rating
workBook = xlrd.open_workbook('F:\Desktop\est3.xls');
# 1.获取sheet的名字
allSheetNames = workBook.sheet_names();
 # 2. 获取sheet内容
## 2.1 法1：按索引号获取sheet内容
sheet1_content1 = workBook.sheet_by_index(0); # sheet索引从0开始
# 3. sheet的名称，行数，列数
print(sheet1_content1.name,sheet1_content1.nrows,sheet1_content1.ncols);

# 4. 获取整行和整列的值（数组）
#rows = sheet1_content1.row_values(3); # 获取第四行内容
col1 = sheet1_content1.col_values(0); # 获取第一列内容
col2 = sheet1_content1.col_values(1); # 获取第二列内容
col3 = sheet1_content1.col_values(2); # 获取第三列内容


rating = []    #二维数组存储所有已知评分情况（workerid,taskid,rating)
rating.append([2,105,5])
rating.append([2,180,5])

tasknum = {}      #10个task，每个task的worker数量
for i in range(1,11):
    tasknum[i] = 0

for t in range(80):  #执行32轮，确保10个task每个都被8个worker完成
    movieuncertainty = {}   #存储每一个task的不确定性
    for taskid in range(1,11):#针对每一个task求不确定性
        sum=0
        valuenum = {}   #每一个值的数量
        for i in range(1,6):   #valuenum的初始化
            valuenum[i] = 0
        for i in range(len(rating)):   #计算valuenun
            if rating[i][1] == taskid:
                sum +=1
                value = int(rating[i][2])
                valuenum[value] =valuenum.get(value)+1
        data = pd.Series(valuenum)    #对valuenum转换成series并排序寻找最大值和第二大值所对应的key
        data = data.sort_values()
        max2valuekey = data.keys()[-2]
        maxvaluekey = data.keys()[-1]
        minen = 0   #计算最小熵
        for key in valuenum.keys():
            a = valuenum[key]
            if key == maxvaluekey:
                a += 1
            p = float(a)/float(1+sum)
            if p==0:
                signlevalueen = 0
            else:
                signlevalueen = p * math.log(p, 2)
            minen -= signlevalueen
        maxen = 0   #计算最大熵
        for key in valuenum.keys():
            a = valuenum[key]
            if key==max2valuekey:
                a += 1
            p = float(a)/float(1+sum)
            if p==0:
                signlevalueen = 0
            else:
                signlevalueen = p * math.log(p, 2)
            maxen -= signlevalueen
        uncertain = maxen - minen
        movieuncertainty[taskid] = uncertain


    data = pd.Series(movieuncertainty)    #对valuenum转换成series并排序寻找最大值和第二大值所对应的key
    data = data.sort_values(ascending=False)

    for i in range(0,10):
        maxunkey = data.keys()[i]
        allocatedtask = maxunkey
        if tasknum[allocatedtask] < 8:  #需要选择worker对其回答
            candidate = []  # 候选列表保存对这个任务进行了回答的所有worker集合
            answer = {}  # 回答字典保存了所有回答问题的worker的答案
            for i in range(0, len(col1)):
                if col2[i] == allocatedtask:  # 此处allocatedtask即为待分配的task序号
                    candidate.append(int(col1[i]))
                    answer[int(col1[i])] = col3[i]
            winner = random.choice(candidate)  # 随机选取1个worker
            rating.append([winner,allocatedtask,answer[winner]])
            tasknum[allocatedtask] = tasknum.get(allocatedtask)+1
            break

print rating
print movieuncertainty

estimatedtruth = []
errorsun = 0
for i in range(1,11):
    ansnum = {}
    for j in range(0,len(rating)):
        if rating[j][1] == i:
            res = int(rating[j][2])
            ansnum[res] = ansnum.get(res,0) + 1
    ansnum = sorted(ansnum.iteritems(), key=lambda d: d[1], reverse=True)  # 对ansnum进行排序
    print (i,"task's score",ansnum[0][0])
    estimatedtruth.append(ansnum[0][0])
    errorsun += abs(ansnum[0][0]-tru2[i-1])
print errorsun/len(estimatedtruth)    #误差errorrate
error = []
for i in range(len(estimatedtruth)):
    error.append(tru2[i]-estimatedtruth[i])
print error
squarederror = []   #计算RMSE
sqerrorsum = 0
for val in error:
    squarederror.append(val*val)
    sqerrorsum += val*val
RMSE = sqrt(sqerrorsum / len(squarederror))
print ("RMSE:",RMSE)

end_time = time()
run_time = end_time - begin_time
print run_time