# coding=utf-8

# ------------------------------链家出租房代码---------------------------
from bs4 import BeautifulSoup  # 网页解析，获取数据
import re  # 正则表达式，进行文字匹配
import xlwt  # 进行excel操作
import requests
from fake_useragent import UserAgent


#  ----------------------------------------
# 创建正则表达式，表示规则（字符串的模式）   re.S 让换行符包含在字符中
findname = re.compile(r'href=".*">(.*?)</a>',re.S)  # 名称
findqu = re.compile(r'target="_blank">(.*?)</a>', re.S)  # 小区
findhuxing = re.compile(r'(\d)室(\d)厅(\d)卫', re.S)  # 户型
findm2 = re.compile(r'(\d+)㎡', re.S)  # 面积
findprice = re.compile(r'<em>(.*?)</em>',re.S)  # 价格
cop = re.compile("[^\u4e00-\u9fa5^.^a-z^A-Z^0-9]")   # 解决字符问题
chinese = re.compile(r'[^\u4e00-\u9fa5]') # 仅保留中文字符
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
    all_list = []
    for page in range(1,101):
        html = askURL(baseurl + str(page) + '/#contentList')
        soup = BeautifulSoup(html, "html.parser")
        soup = soup.find('div', class_="content__article")
        try:
            for home in soup.find_all('div' , class_ = 'content__list--item--main'):
                home_info = []
                # 得到租房名称
                name = str(home.find('p', class_ = "content__list--item--title"))
                name = re.findall(findname,name)
                name = name[0].strip()   # 得到名字
                home_info.append(name)

                # 得到地理位置
                home_info.append(html_scname)
                home_info.append(html_cname)
                location = home.find('p', class_="content__list--item--des")
                qu =str(location.find_all('a')).split(',')
                # 分类讨论
                if len(qu) < 2:
                    home_info.extend(['','',''])
                else:
                    for i in qu:
                        i = re.sub(chinese,'',i)
                        home_info.append(i)
                # 得到具体大小 户型

                info = str(home.find('p', class_="content__list--item--des"))
                m2 = re.findall(findm2,info)
                m2 = m2[0]
                home_info.append(m2)
                shi = re.findall(findhuxing,info)
                try:
                    huxing = shi[0][0] + '室' + shi[0][1] + '厅' + shi[0][2] + '卫'
                except IndexError:
                    huxing = ''
                home_info.append(huxing)

                # 找到价格
                price = str(home.find('span', class_ ="content__list--item-price"))
                price = re.findall(findprice,price)[0]
                home_info.append(price)
                all_list.append(home_info)
        except AttributeError:
            continue

        print('得到' + html_scname + html_cname + '第'+str(page)+'页数据' )

    all_list.insert(0,['名称','省','市','区域', '具体位置', '小区名称' , '大小（平方米）','户型','价格（元/月）'])
    return all_list


def savedata(datalist):  # 3、保存数据
    worksheet = workbook.add_sheet(html_scname + html_cname)  # 创建工作表
    for i in range(int(len(datalist))):
        data = datalist[i]
        for j in range(9):
            worksheet.write(i, j, data[j])  # 数据录入


if __name__ == "__main__":

    html_name = input('请输入要爬取城市的英文名：')
    html_scname = input('请输入要爬取省的中文名：')
    html_cname = input('请输入要爬取市的中文名：')
    workbook = xlwt.Workbook(encoding='utf-8', style_compression=0)  # 创建workbook
    baseurl = "https://" + html_name + ".lianjia.com/zufang/pg"  # 2/#contentList"
    list = getdata(baseurl)
    savedata(list)
    workbook.save('./数据/' + html_scname + html_cname + '.xls')
    print('爬取完成')