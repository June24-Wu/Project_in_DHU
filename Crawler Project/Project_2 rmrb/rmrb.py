# coding=utf-8

from bs4 import BeautifulSoup # 网页解析，获取数据
import re # 正则表达式，进行文字匹配
import urllib.request, urllib.error # 制定URL,获取网页数据
import xlwt # 进行excel操作

def main():
    baseurl = "http://laoziliao.net/rmrb/"
    yearlist = yearlistfunction()
    datalist = getdata(yearlist,baseurl)
    savepath = 'rmrb.xls'
    savedata(datalist,savepath)

#  ----------------------------------------
# 创建正则表达式，表示规则（字符串的模式）   re.S 让换行符包含在字符中
# findbanben= re.compile(r'<h3>(.*?)</h3>')   # 版本号
# findlink = re.compile(r'<li>◆<a href="(.*?)">', re.S)  # 链接
findname= re.compile(r'<li>◆<a href="*(.*?)</a></li>', re.S)  # 文章的名字
# findrating = re.compile(r'<span class="rating_num" property="v:average">(.*?)</span>', re.S) # 找到影片评分
# findpeople = re.compile(r'<span>(\d*)人评价</span>', re.S)  # 找到评价人数 (\d*) 寻找数字
# findjieshao = re.compile(r'<span class="inq">(.*?)</span>', re.S)  # 找到介绍
# findbd = re.compile(r'<p class="">(.*?)</p>', re.S)  # 找到主演，导演
# --------------------------------------------------
def yearlistfunction():

    month_day = [[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31], [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]]

    s_year =  int(input('开始年：'))
    s_month =int(input('开始月：'))
    s_date = int(input('开始日：'))

    # 结束年月日
    e_year = int(input('结束年：'))
    e_month = int(input('结束月：'))
    e_date =  int(input('结束日：'))

    # 打印年月日
    datelist = []
    for now_year in range(s_year, e_year + 1):
        if now_year % 4 == 0:
            mr = 1
        else:
            mr = 0  # 选取闰年
        if now_year == s_year:
            first_month = s_month
        else:
            first_month = 1
        if now_year == e_year:
            last_month = e_month
            month_day[mr][last_month - 1] = e_date
        else:
            last_month = 12
        for now_month in range(first_month, last_month + 1):
            month_day_max = month_day[mr][now_month - 1]
            if now_year == s_year:
                for day in range(s_date,month_day_max + 1):
                    date = str(now_year) + '-' + str(now_month) + '-' + str(day)  # 打印出日期
                    datelist.append(date)
            else:
                for day in range(1, month_day_max + 1):
                    date = str(now_year) + '-' + str(now_month) + '-' + str(day)  # 打印出日期
                    datelist.append(date)
    return datelist



def askURL(url):   # 访问网站的函数
    head = {  # 模拟浏览器头部信息，豆瓣服务器发送消息
        # 服务代理，告诉豆瓣服务器，我们是什么类型的机器，本质是我们可以接受什么文件内容
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
    }
    data = bytes(urllib.parse.urlencode({'name': 'eric'}), encoding='utf-8')
    request = urllib.request.Request(url, headers=head, data=data, method="POST")  # 发送请求
    try:
        response = urllib.request.urlopen(request)    # 取得响应
        html = response.read().decode('utf-8')   # 获取网页内容
    except urllib.error.URLError as e:
        if hasattr(e,'code'):
            print(e.code)
        if hasattr(e,'reason'):
            print(e.reason)
    return html

def getdata(yearlist,baseurl):
    datalist = []
    for i in range(len(yearlist)):   # 调用获取页面信息的函数
        url = baseurl + yearlist[i]
        html = askURL(url)    # 保存获取到的网页源码
        print(html)
        # 2、解析数据（在for循环里面，逐一解析网页）
        soup = BeautifulSoup(html,"html.parser")
        for item in soup.find_all('div', class_ = 'box'):  #查找符合要求的字符串，形成列表
            # print(item) # 测试，查看人民日报item全部信息
            # data = [] # 保存一个日期人民日报的所有信息
            item = str(item)


           # banben = re.findall(findbanben,item)   # 获取版本号
           # print(banben) # 测试，查看所有的版本

            # link = re.findall(findlink,item)
            # print(link)
            name = re.findall(findname,item)
            for t in range(len(name)):
                name[t] = name[t].split(r'">')
            name.insert(0,[yearlist[i],''])
            datalist += name
    print(datalist)
    return datalist

def savedata(datalist,savepath):  # 3、保存数据
    workbook = xlwt.Workbook(encoding='utf-8',style_compression=0)  # 创建workbook
    worksheet = workbook.add_sheet('豆瓣电影TOP250')  # 创建工作表
    col = ('链接','文章名')
    for i in range(2):
        worksheet.write(0,i,col[i])   # 添加列明
    for i in range(len(datalist)):
        print('第%d条' % (i+1))
        data = datalist[i]
        for j in range(2):
            worksheet.write(i+1,j,data[j])   # 数据录入
    workbook.save(savepath)

main()
print('爬取完毕')
