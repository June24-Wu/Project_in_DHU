# coding=utf-8
from bs4 import BeautifulSoup  # 网页解析，获取数据
import re  # 正则表达式，进行文字匹配
import xlwt  # 进行excel操作
import requests
from fake_useragent import UserAgent
import pymysql

db1 = pymysql.connect(host="localhost", user="root", password='Wwj0233tt.', charset='utf8')
cursor = db1.cursor()


def main():
    baseurl = "http://www.xingdd.com/schools.html"
    getdata(baseurl)


#  ----------------------------------------
# 创建正则表达式，表示规则（字符串的模式）   re.S 让换行符包含在字符中
findqu = re.compile(r'<dt>\n(.*?)\n</dt>',re.S)  # 找到每个区
findschool = re.compile(r'title=.*>(.*?)</a>', re.S)  # 学校名字链接
findlink = re.compile(r'href=(.*?)title.*', re.S)  # 链接
cop = re.compile("[^\u4e00-\u9fa5^.^a-z^A-Z^0-9]")   #解决字符问题
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
    html = askURL(baseurl)
    soup = BeautifulSoup(html, "html.parser")
    soup = soup.find('div', class_="row mlm mrm")
    html = list(soup.find_all('dl'))   # 找到每个dl,返回一个列表
    for q in html:
        datalist = []
        q1 = q.find_all('dt')
        qu = str(q1)
        qu=qu.replace(' ','').replace('</dt>','').replace('<dt>','').replace('\n', '').replace('\r', '')
        datalist.append(qu)
        schoollist = []
        linklist = []
        for item in q.find_all('dd'):
            school = str(item)
            school = re.findall(findschool,school)
            schoollist.append(school)
        datalist.append(schoollist)
        for item in q.find_all('a'):
            link = item['href']
            linklist.append(link)
        datalist.append(linklist)
        # print(datalist) #------------------------------------ 得到每个区，每个学习，每个链接


        # ----------------------------------------------开始访问每个具体学校的受众小区网站
        list2 = []
        for i in range(len(datalist[1])):
            schoolname = datalist[1][i]
            linkname = datalist[2][i]
            html2 = askURL('http://www.xingdd.com/' + linkname)
            soup = BeautifulSoup(html2, "html.parser")
            soup = soup.find('div', class_="mbm label-list")
            homelist = []
            for i in soup.find_all('a'):
                i = i['name']
                i = str(i)
                homelist.append(i)
            list2.append(schoolname)
            list2.append(homelist)
        list2.insert(0,datalist[0])
        print(list2)
        savesql(list2)
        print('保存成功一条数据')
        # ------------------------------------------------开始保存数据



def savesql(datalist):  # 保存到数据库
    database = datalist[0].replace('[','').replace(']','')
    db1 = pymysql.connect(host="localhost", user="root", password='Wwj0233tt.', charset='utf8')
    cursor1 = db1.cursor()
    drop = f"""DROP DATABASE IF EXISTS %s""" % database
    cursor1.execute(drop)
    create = """CREATE DATABASE %s""" % database
    cursor1.execute(create)
    db = pymysql.connect(host="localhost", user="root", password='Wwj0233tt.', charset='utf8', db=database)  # 创建数据库
    cursor = db.cursor()  # 创建游标
    for i in range(1,int(1+(int(len(datalist))-1)/2)):
        datalist[2 * i - 1][0] = cop.sub('',datalist[2 * i - 1][0])
        sql = f"""CREATE TABLE {datalist[2 * i - 1][0]}(涉及小区 varchar(20))"""
        cursor.execute(sql)
        for t in datalist[2*i]:
            insert = f"""INSERT INTO %s(涉及小区) VALUES('%s')""" % (datalist[2*i-1][0],t)
            cursor.execute(insert)
            db.commit()
        db.commit()
    db.commit()
main()
db1.close()
print('爬取完毕')
