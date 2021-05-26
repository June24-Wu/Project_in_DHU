# coding=utf-8

from bs4 import BeautifulSoup # 网页解析，获取数据
import re # 正则表达式，进行文字匹配
import urllib.request, urllib.error # 制定URL,获取网页数据
import xlwt # 进行excel操作

def main():
    baseurl = "https://m.dongqiudi.com/article/1560121.html"
    getdata(baseurl)
    # savepath = 'rmrb.xls'
    # savedata(datalist,savepath)

#  ----------------------------------------
# 创建正则表达式，表示规则（字符串的模式）   re.S 让换行符包含在字符中
# findbanben= re.compile(r'<h3>(.*?)</h3>')   # 版本号
# findlink = re.compile(r'<li>◆<a href="(.*?)">', re.S)  # 链接
# findname= re.compile(r'<li>◆<a href="*(.*?)</a></li>', re.S)  # 文章的名字
# findrating = re.compile(r'<span class="rating_num" property="v:average">(.*?)</span>', re.S) # 找到影片评分
# findpeople = re.compile(r'<span>(\d*)人评价</span>', re.S)  # 找到评价人数 (\d*) 寻找数字
# findjieshao = re.compile(r'<span class="inq">(.*?)</span>', re.S)  # 找到介绍
# findbd = re.compile(r'<p class="">(.*?)</p>', re.S)  # 找到主演，导演
# --------------------------------------------------

def askURL(url):   # 访问网站的函数
    head = {  # 模拟浏览器头部信息，豆瓣服务器发送消息
        # 服务代理，告诉豆瓣服务器，我们是什么类型的机器，本质是我们可以接受什么文件内容
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
        'Accept': 'text / html, application / xhtml + xml, application / xml;0.9, image / webp, image / apng, * / *;q = 0.8, application / signed - exchange;v = b3;q = 0.9',
        'Accept - Encoding': 'gzip, deflate, br',
        'Accept - Language': 'zh - CN, zh;q = 0.9'}
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

def getdata(baseurl):
    datalist = []
    for i in range(1):   # 调用获取页面信息的函数
        url = baseurl
        html = askURL(url)    # 保存获取到的网页源码
        print(html)
        # 2、解析数据（在for循环里面，逐一解析网页）
        soup = BeautifulSoup(html,"html.parser")
        for item in soup.find_all('artical', class_ = 'show-more'):  #查找符合要求的字符串，形成列表
            item = str(item)
            print(item) # 测试，查看人民日报item全部信息
            # data = [] # 保存一个日期人民日报的所有信息



           # banben = re.findall(findbanben,item)   # 获取版本号
           # print(banben) # 测试，查看所有的版本

            # link = re.findall(findlink,item)
            # print(link)
    #         name = re.findall(findname,item)
    #         for t in range(len(name)):
    #             name[t] = name[t].split(r'">')
    #         name.insert(0,[yearlist[i],''])
    #         datalist += name
    # print(datalist)
    # return datalist

# def savedata(datalist,savepath):  # 3、保存数据
#     workbook = xlwt.Workbook(encoding='utf-8',style_compression=0)  # 创建workbook
#     worksheet = workbook.add_sheet('豆瓣电影TOP250')  # 创建工作表
#     col = ('链接','文章名')
#     for i in range(2):
#         worksheet.write(0,i,col[i])   # 添加列明
#     for i in range(len(datalist)):
#         print('第%d条' % (i+1))
#         data = datalist[i]
#         for j in range(2):
#             worksheet.write(i+1,j,data[j])   # 数据录入
#     workbook.save(savepath)

main()
print('爬取完毕')
