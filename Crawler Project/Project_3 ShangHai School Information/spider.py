# coding=utf-8
from bs4 import BeautifulSoup  # 网页解析，获取数据
import re  # 正则表达式，进行文字匹配
import xlwt  # 进行excel操作
import requests
from fake_useragent import UserAgent
import pymysql

db1 = pymysql.connect(host="localhost", user="root", password='Wwj0233tt.', charset='utf8')
cursor1 = db1.cursor()
drop = """DROP DATABASE IF EXISTS 上海市中小学生入学情况"""
cursor1.execute(drop)
create = """CREATE DATABASE 上海市中小学生入学情况"""
cursor1.execute(create)
db1.close()


def main():
    baseurl = "http://www.shmeea.edu.cn/20200724/"
    getdata(baseurl)


#  ----------------------------------------
# 创建正则表达式，表示规则（字符串的模式）   re.S 让换行符包含在字符中
findmingdan = re.compile(r'width:630pt" width="840">(.*?)</td>')  # 名单名称
findbiaoti = re.compile(r'width:210pt" width="280">(.*?)</td>', re.S)  # 链接
# --------------------------------------------------

def askURL(url):
    headers = {"User-Agent": UserAgent(verify_ssl=False).random}
    response = requests.get(url, headers=headers)  # 用UserAgent的方法来访问网页

    if response.encoding == 'ISO-8859-1':
        encodings = requests.utils.get_encodings_from_content(response.text)
        if encodings:
            encoding = encodings[0]
        else:
            encoding = response.apparent_encoding
    else:
        encoding = response.encoding
    response = response.content.decode(encoding, 'ignore').encode('utf-8', 'ignore')

    return response


def getdata(baseurl):
    for l in range(1, 77):
        l = str(l).rjust(2, '0')  # 调用获取页面信息的函数
        url = baseurl + l + '.htm'
        html = askURL(url)  # 保存获取到的网页源码
        # 2、解析数据（在for循环里面，逐一解析网页）
        soup = BeautifulSoup(html, "html.parser")
        for item in soup.find_all('div', align="center"):  # 查找符合要求的字符串，形成列表
            # print(item) # 测试，查看人民日报item全部信息
            item = str(item).split('<tr height="17" style="height:12.75pt">')
            if len(item) == 4:  # 多个名单的去除
                item.pop(1)
                item.pop(1)
            for i in item:
                data = []
                mingdan = re.findall(findmingdan, i)  # 获取版本号
                mingdan.append('')
                mingdan.append('')
                data.append(mingdan)
                biaoti = re.findall(findbiaoti, i)
                for t in range(1, int((len(biaoti) + 1) / 3)):
                    data.append(biaoti[(t - 1) * 3:(t * 3)])
                if int(l) == 58:
                    data[18][2] = '李丁'

                savedata(data)
                savesql(data)
        print('打印出第%d条数据' % int(l))


def savedata(datalist):  # 3、保存数据
    workbook = xlwt.Workbook(encoding='utf-8', style_compression=0)  # 创建workbook
    worksheet = workbook.add_sheet('sheet1')  # 创建工作表
    for i in range(int(len(datalist))):
        data = datalist[i]
        for j in range(3):
            worksheet.write(i, j, data[j])  # 数据录入
    workbook.save('./数据/' + str(datalist[0][0]) + '.xls')


def savesql(datalist):  # 保存到数据库
    database = '上海市中小学生入学情况'  # 数据库名称
    db = pymysql.connect(host="localhost", user="root", password='Wwj0233tt.', charset='utf8', db=database)  # 创建数据库
    cursor = db.cursor()  # 创建游标
    table = datalist[0][0]

    sql = """CREATE TABLE %s ( 序号 varchar(20), 考生报名号 varchar(50), 姓名 varchar(20) )""" % table
    cursor.execute(sql)

    for i in range(2, int(len(datalist))):
        insert = """INSERT INTO %s(序号,考生报名号,姓名) VALUES('%s','%s','%s')""" % (
        table, datalist[i][0], datalist[i][1], datalist[i][2])
        cursor.execute(insert)
    db.commit()
    db.close()


main()
print('爬取完毕')
