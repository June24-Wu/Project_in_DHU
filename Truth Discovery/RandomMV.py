#coding:utf-8
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

moviesum={}     #每个movie总分
number={}   #每个movie评分数量
for i in range(0,len(col1)):
    movie=int(col2[i])
    value=col3[i]
    moviesum[movie]=moviesum.get(movie,0)+value
    number[movie]=number.get(movie,0)+1
aver={}   #每个movie平均分 aver是字典，从1开始
for key in moviesum.keys():
    aver[key]=moviesum[key]/number[key]
print aver

estimatedtruth = []
errorsun = 0
for m in range(1,11):
    candidate = []    #候选列表保存对这个任务进行了回答的所有worker集合
    answer = {}      #回答字典保存了所有回答问题的worker的答案
    ansnum = {}      #答案数量字典保存选中的worker对每个答案回答的数量
    for i in range(0,len(col1)):
        if col2[i] == m:   #此处m即为待分配的task序号
            candidate.append(int(col1[i]))
            answer[int(col1[i])] = col3[i]
    winner = random.sample(candidate,8)   #随机选取8个worker
    for i in range(8):    #统计被选取的worker各个答案的数量
        ansnum[answer[winner[i]]] = ansnum.get(answer[winner[i]],0)+1
    ansnum = sorted(ansnum.iteritems(), key=lambda d: d[1], reverse=True)    #对ansnum进行排序
    print (m,"task's score",ansnum[0][0])
    estimatedtruth.append(ansnum[0][0])
    errorsun += abs(ansnum[0][0]-tru2[m-1])
print errorsun/len(estimatedtruth)    #误差errorrate
error = []
for i in range(len(estimatedtruth)):
    error.append(tru2[i]-estimatedtruth[i])
print error
squarederror = []
sqerrorsum = 0
for val in error:
    squarederror.append(val*val)
    sqerrorsum += val*val
RMSE = sqrt(sqerrorsum / len(squarederror))
print ("RMSE:",RMSE)

end_time = time()
run_time = end_time - begin_time
print run_time