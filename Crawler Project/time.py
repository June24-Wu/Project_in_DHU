# coding=utf-8
import random
import json
import commctrl
import re
import os

cmd1 = "curl http://laoziliao.net/rmrb/"

#  第二是闰年
month_day = [[31,28,31,30,31,30,31,31,30,31,30,31],[31,29,31,30,31,30,31,31,30,31,30,31]]

# 开始年月日
s_year = 1950
s_month = 2
s_date = 28

# 结束年月日
e_year = 1950
e_month = 3
e_date = 10

# 打印年月日
for now_year in range(s_year,e_year+1):
    if now_year % 4 == 0:
        mr = 1
    else:
        mr = 0 # 选取闰年
    if now_year == s_year:
        first_month = s_month
    else:
        first_month = 1
    if now_year == e_year:
        last_month = e_month
        month_day[mr][last_month - 1] = e_date
    else:
        last_month = 12
    for now_month in range(first_month,last_month + 1):
        month_day_max = month_day[mr][now_month-1]
        for day in range(1,month_day_max+1):
            date = str(now_year) + '-' + str(now_month) + '-' + str(day)  # 打印出日期
            cmdline = cmd1 + date + ' > ' + '爬虫/sub_index/index_' + date +'.html'
            os.system(cmdline)





